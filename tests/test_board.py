"""
Board System Tests

Tests for game board functionality including:
- Board initialization and state
- Cell management
- Line detection and clearing logic
"""

from src.game.board import Board


def test_board_initialization():
    """Test that board initializes correctly."""
    board = Board()

    assert board.width == 10
    assert board.height == 20
    assert len(board.grid) == 10  # grid[x] where x is column (width)
    assert len(board.grid[0]) == 20  # grid[x][y] where y is row (height)

    # All cells should be empty initially
    for column in board.grid:
        for cell in column:
            assert cell is None


def test_cell_operations():
    """Test setting and getting cell values."""
    board = Board()

    # Test setting a cell
    color = (255, 0, 0)  # Red
    board.set_cell(5, 10, color)
    assert board.get_cell(5, 10) == color

    # Test getting empty cell
    assert board.get_cell(3, 5) is None

    # Test out-of-bounds
    assert board.get_cell(-1, 0) is None
    assert board.get_cell(10, 0) is None
    assert board.get_cell(0, -1) is None
    assert board.get_cell(0, 20) is None


def test_line_completion_check():
    """Test line completion detection."""
    board = Board()

    # Fill a complete line
    for x in range(board.width):
        board.set_cell(x, 19, (255, 255, 255))

    assert board.is_line_complete(19)
    assert not board.is_line_complete(18)


def test_board_clear():
    """Test board clearing functionality."""
    board = Board()

    # Add some pieces to the board
    board.set_cell(5, 10, (255, 0, 0))
    board.set_cell(3, 15, (0, 255, 0))

    # Clear the board
    board.clear_board()

    # All cells should be empty
    for column in board.grid:
        for cell in column:
            assert cell is None


def test_piece_collision_detection():
    """Test collision detection with pieces."""
    from src.game.piece import Piece, PieceType

    board = Board()

    # Test I-piece at valid position
    i_piece = Piece(PieceType.I, 5, 10)
    assert board.is_valid_position(i_piece)

    # Test I-piece at invalid position (out of bounds)
    i_piece_out = Piece(PieceType.I, 8, 10)  # Will extend beyond right edge
    assert not board.is_valid_position(i_piece_out)

    # Test I-piece at bottom edge
    i_piece_bottom = Piece(PieceType.I, 5, 19)  # At bottom row
    assert board.is_valid_position(i_piece_bottom)

    # Test I-piece below bottom (invalid)
    i_piece_below = Piece(PieceType.I, 5, 20)  # Below bottom
    assert not board.is_valid_position(i_piece_below)


def test_piece_placement():
    """Test placing pieces on the board."""
    from src.game.piece import Piece, PieceType

    board = Board()
    piece = Piece(PieceType.O, 5, 10)

    # Place piece successfully
    board.place_piece(piece)

    # Check that cells are filled
    cells = piece.get_cells()
    for x, y in cells:
        assert board.get_cell(x, y) == piece.color

    # Try to place overlapping piece (should fail)
    overlapping_piece = Piece(PieceType.I, 5, 10)
    try:
        board.place_piece(overlapping_piece)
        assert False, "Should have raised ValueError for overlapping piece"
    except ValueError:
        pass  # Expected


def test_line_clearing():
    """Test line clearing functionality."""
    board = Board()

    # Fill a complete line at the bottom
    for x in range(board.width):
        board.set_cell(x, 19, (255, 255, 255))

    # Add some blocks above the line
    board.set_cell(3, 17, (255, 0, 0))
    board.set_cell(7, 18, (0, 255, 0))

    # Clear completed lines
    lines_cleared = board.clear_completed_lines()

    # Should have cleared 1 line
    assert lines_cleared == 1

    # Bottom row should now be empty
    assert not board.is_line_complete(19)

    # Blocks should have fallen down
    assert board.get_cell(3, 18) == (255, 0, 0)  # Moved down
    assert board.get_cell(7, 19) == (0, 255, 0)  # Moved down


def test_multiple_line_clearing():
    """Test clearing multiple lines at once."""
    board = Board()

    # Fill two complete lines
    for x in range(board.width):
        board.set_cell(x, 18, (255, 255, 255))
        board.set_cell(x, 19, (0, 0, 255))

    # Add a block above
    board.set_cell(5, 17, (255, 0, 0))

    # Clear completed lines
    lines_cleared = board.clear_completed_lines()

    # Should have cleared 2 lines
    assert lines_cleared == 2

    # Both lines should be empty
    assert not board.is_line_complete(18)
    assert not board.is_line_complete(19)

    # Block should have fallen down 2 positions
    assert board.get_cell(5, 19) == (255, 0, 0)


def test_game_over_detection():
    """Test game over detection."""
    board = Board()

    # Initially not game over
    assert not board.is_game_over()

    # Fill top row
    for x in range(board.width):
        board.set_cell(x, 0, (255, 255, 255))

    # Should be game over now
    assert board.is_game_over()

    # Clear board
    board.clear_board()
    assert not board.is_game_over()


def test_board_boundaries():
    """Test board boundary handling."""
    board = Board()

    # Test valid positions
    assert board.get_cell(0, 0) is None
    assert board.get_cell(9, 19) is None

    # Test invalid positions (should return None)
    assert board.get_cell(-1, 0) is None
    assert board.get_cell(10, 0) is None
    assert board.get_cell(0, -1) is None
    assert board.get_cell(0, 20) is None

    # Test setting invalid positions (should be ignored)
    board.set_cell(-1, 0, (255, 0, 0))
    board.set_cell(10, 0, (255, 0, 0))
    assert board.get_cell(-1, 0) is None
    assert board.get_cell(10, 0) is None
