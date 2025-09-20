"""
Piece System Tests

Tests for Tetrimino piece functionality including:
- Piece creation and initialization
- Shape definitions and rotations
- Movement and position tracking
"""

from src.game.piece import Piece, PieceType
from src.game.piece_factory import PieceFactory


def test_piece_creation():
    """Test that pieces can be created with correct properties."""
    piece = Piece(PieceType.I, 5, 10)

    assert piece.piece_type == PieceType.I
    assert piece.x == 5
    assert piece.y == 10
    assert piece.rotation == 0


def test_piece_colors():
    """Test that each piece type has a unique color."""
    colors = set()

    for piece_type in PieceType:
        piece = Piece(piece_type)
        color = piece.color
        assert color not in colors, f"Duplicate color for {piece_type}"
        colors.add(color)


def test_i_piece_shapes():
    """Test I-piece shape definitions."""
    piece = Piece(PieceType.I)

    # Test horizontal orientation (rotation 0)
    shape = piece.get_current_shape()
    assert shape == [[1], [1], [1], [1]]

    # Test vertical orientation (rotation 1)
    piece.rotate_clockwise()
    shape = piece.get_current_shape()
    assert shape == [[1, 1, 1, 1]]


def test_o_piece_shapes():
    """Test O-piece shape (should not change with rotation)."""
    piece = Piece(PieceType.O)
    original_shape = piece.get_current_shape()

    # Rotate through all orientations
    for _ in range(4):
        piece.rotate_clockwise()
        assert piece.get_current_shape() == original_shape


def test_piece_rotation():
    """Test piece rotation mechanics."""
    piece = Piece(PieceType.T)

    # Test clockwise rotation
    original_rotation = piece.rotation
    piece.rotate_clockwise()
    assert piece.rotation == (original_rotation + 1) % 4

    # Test counterclockwise rotation
    piece.rotate_counterclockwise()
    assert piece.rotation == original_rotation


def test_piece_movement():
    """Test piece movement functionality."""
    piece = Piece(PieceType.T, 5, 10)

    # Test horizontal movement
    piece.move(2, 0)
    assert piece.x == 7
    assert piece.y == 10

    # Test vertical movement
    piece.move(0, 3)
    assert piece.x == 7
    assert piece.y == 13


def test_piece_factory():
    """Test piece factory functionality."""
    factory = PieceFactory()

    # Test random piece creation
    piece = factory.create_random_piece()
    assert isinstance(piece, Piece)
    assert piece.piece_type in PieceType

    # Test specific piece creation
    t_piece = factory.create_piece(PieceType.T)
    assert t_piece.piece_type == PieceType.T


def test_all_piece_shapes():
    """Test that all 7 piece types have proper shape definitions."""
    for piece_type in PieceType:
        piece = Piece(piece_type)

        # Each piece should have at least one shape
        assert len(piece.shapes) > 0

        # Each shape should be a 2D list
        for shape in piece.shapes:
            assert isinstance(shape, list)
            assert len(shape) > 0
            assert all(isinstance(row, list) for row in shape)

        # Test that rotation cycles work properly
        original_rotation = piece.rotation
        for _ in range(len(piece.shapes) * 2):
            piece.rotate_clockwise()
        assert piece.rotation == original_rotation


def test_s_piece_shapes():
    """Test S-piece specific shape definitions."""
    piece = Piece(PieceType.S)

    # S-piece should have 2 rotations
    assert len(piece.shapes) == 2

    # Test both rotation states
    shape0 = piece.get_current_shape()
    piece.rotate_clockwise()
    shape1 = piece.get_current_shape()

    # Shapes should be different
    assert shape0 != shape1


def test_z_piece_shapes():
    """Test Z-piece specific shape definitions."""
    piece = Piece(PieceType.Z)

    # Z-piece should have 2 rotations
    assert len(piece.shapes) == 2

    # Test both rotation states
    shape0 = piece.get_current_shape()
    piece.rotate_clockwise()
    shape1 = piece.get_current_shape()

    # Shapes should be different
    assert shape0 != shape1


def test_j_piece_shapes():
    """Test J-piece specific shape definitions."""
    piece = Piece(PieceType.J)

    # J-piece should have 4 rotations
    assert len(piece.shapes) == 4

    # Test all rotation states
    shapes = []
    for _ in range(4):
        shapes.append(piece.get_current_shape())
        piece.rotate_clockwise()

    # All shapes should be different
    assert len(set(str(s) for s in shapes)) == 4


def test_l_piece_shapes():
    """Test L-piece specific shape definitions."""
    piece = Piece(PieceType.L)

    # L-piece should have 4 rotations
    assert len(piece.shapes) == 4

    # Test all rotation states
    shapes = []
    for _ in range(4):
        shapes.append(piece.get_current_shape())
        piece.rotate_clockwise()

    # All shapes should be different
    assert len(set(str(s) for s in shapes)) == 4


def test_get_cells():
    """Test get_cells method functionality."""
    # Test S-piece at specific position
    s_piece = Piece(PieceType.S, 5, 10)
    cells = s_piece.get_cells()

    # Should return list of tuples
    assert isinstance(cells, list)
    assert all(isinstance(cell, tuple) for cell in cells)
    assert all(len(cell) == 2 for cell in cells)

    # Test I-piece at origin
    i_piece = Piece(PieceType.I, 0, 0)
    cells = i_piece.get_cells()

    # I-piece horizontal should have 4 cells
    assert len(cells) == 4
    assert (0, 0) in cells
    assert (1, 0) in cells
    assert (2, 0) in cells
    assert (3, 0) in cells


def test_piece_copy():
    """Test piece copy functionality."""
    original = Piece(PieceType.T, 5, 10)
    original.rotate_clockwise()

    copy_piece = original.copy()

    # Should be same type and position
    assert copy_piece.piece_type == original.piece_type
    assert copy_piece.x == original.x
    assert copy_piece.y == original.y
    assert copy_piece.rotation == original.rotation

    # Should be independent objects
    assert copy_piece is not original

    # Modifying copy shouldn't affect original
    copy_piece.move(1, 1)
    assert original.x == 5
    assert original.y == 10


def test_piece_factory_all_pieces():
    """Test create_all_pieces method."""
    factory = PieceFactory()
    all_pieces = factory.create_all_pieces()

    # Should create exactly 7 pieces
    assert len(all_pieces) == 7

    # Should have one of each type
    piece_types = [piece.piece_type for piece in all_pieces]
    assert len(set(piece_types)) == 7

    # All pieces should be at spawn position
    for piece in all_pieces:
        assert piece.x == factory.spawn_x
        assert piece.y == factory.spawn_y
