"""
Piece Factory Tests

Tests for piece factory functionality including:
- Random piece generation
- 7-bag randomization system
- Piece spawning and positioning
"""

from src.game.piece_factory import PieceFactory
from src.game.piece import Piece, PieceType


def test_piece_factory_initialization():
    """Test piece factory initialization."""
    factory = PieceFactory()

    # Should have correct spawn position
    assert factory.spawn_x == 5  # round(10/2)
    assert factory.spawn_y == 0

    # Should have all piece types
    assert len(factory.piece_types) == 7
    assert set(factory.piece_types) == set(PieceType)


def test_specific_piece_creation():
    """Test creating specific piece types."""
    factory = PieceFactory()

    for piece_type in PieceType:
        piece = factory.create_piece(piece_type)

        assert piece.piece_type == piece_type
        assert piece.x == factory.spawn_x
        assert piece.y == factory.spawn_y
        assert piece.rotation == 0


def test_create_all_pieces():
    """Test creating all piece types at once."""
    factory = PieceFactory()
    all_pieces = factory.create_all_pieces()

    # Should create exactly 7 pieces
    assert len(all_pieces) == 7

    # Should have one of each type
    piece_types = [piece.piece_type for piece in all_pieces]
    assert len(set(piece_types)) == 7
    assert set(piece_types) == set(PieceType)

    # All pieces should be at spawn position
    for piece in all_pieces:
        assert piece.x == factory.spawn_x
        assert piece.y == factory.spawn_y


def test_seven_bag_randomization():
    """Test 7-bag randomization system."""
    factory = PieceFactory()

    # Generate 14 pieces (2 complete bags)
    pieces = []
    for _ in range(14):
        piece = factory.create_random_piece()
        pieces.append(piece.piece_type)

    # First 7 pieces should all be different
    first_bag = pieces[:7]
    assert len(set(first_bag)) == 7

    # Second 7 pieces should all be different
    second_bag = pieces[7:14]
    assert len(set(second_bag)) == 7

    # Both bags should contain all piece types
    assert set(first_bag) == set(PieceType)
    assert set(second_bag) == set(PieceType)


def test_seven_bag_distribution():
    """Test that 7-bag system provides fair distribution over time."""
    factory = PieceFactory()

    # Generate many pieces
    piece_counts = {piece_type: 0 for piece_type in PieceType}

    # Generate 70 pieces (10 complete bags)
    for _ in range(70):
        piece = factory.create_random_piece()
        piece_counts[piece.piece_type] += 1

    # Each piece type should appear exactly 10 times
    for piece_type in PieceType:
        assert piece_counts[piece_type] == 10


def test_random_piece_positioning():
    """Test that random pieces are created at correct spawn position."""
    factory = PieceFactory()

    # Generate several random pieces
    for _ in range(20):
        piece = factory.create_random_piece()

        assert piece.x == factory.spawn_x
        assert piece.y == factory.spawn_y
        assert piece.rotation == 0


def test_factory_independence():
    """Test that multiple factory instances are independent."""
    factory1 = PieceFactory()
    factory2 = PieceFactory()

    # Generate pieces from both factories
    pieces1 = [factory1.create_random_piece() for _ in range(7)]
    pieces2 = [factory2.create_random_piece() for _ in range(7)]

    # Both should generate valid pieces
    assert all(isinstance(p, Piece) for p in pieces1)
    assert all(isinstance(p, Piece) for p in pieces2)

    # Each factory should have its own random state
    # (We can't easily test this without mocking, but we can verify they work)


def test_piece_factory_with_different_spawn():
    """Test factory with different spawn position."""
    # This would require modifying the factory to accept spawn position
    # For now, just test the default behavior
    factory = PieceFactory()

    piece = factory.create_piece(PieceType.I)
    assert piece.x == 5  # Default spawn x
    assert piece.y == 0  # Default spawn y
