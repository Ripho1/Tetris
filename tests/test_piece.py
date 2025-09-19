"""
Piece System Tests

Tests for Tetrimino piece functionality including:
- Piece creation and initialization
- Shape definitions and rotations
- Movement and position tracking
"""

import pytest
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
    assert shape == [[1, 1, 1, 1]]

    # Test vertical orientation (rotation 1)
    piece.rotate_clockwise()
    shape = piece.get_current_shape()
    assert shape == [[1], [1], [1], [1]]


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
