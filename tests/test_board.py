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
    assert len(board.grid) == 20
    assert len(board.grid[0]) == 10

    # All cells should be empty initially
    for row in board.grid:
        for cell in row:
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
    for row in board.grid:
        for cell in row:
            assert cell is None
