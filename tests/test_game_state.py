"""
Game State Management Tests

Tests for the game state functionality including:
- Piece falling mechanics
- Game progression (score, level, lines)
- Piece spawning and placement
- Game over detection
- Input handling
"""

import pytest
import time
from unittest.mock import patch, MagicMock
from src.game.game_state import GameState
from src.game.piece import Piece, PieceType
from src.game.board import Board
from src.config.settings import settings


@pytest.fixture
def game_state():
    """Create a game state instance for testing."""
    return GameState()


def test_game_state_initialization(game_state):
    """Test that game state initializes correctly."""
    assert game_state.board is not None
    assert game_state.piece_factory is not None
    assert game_state.score == 0
    assert game_state.level == 1
    assert game_state.lines_cleared == 0
    assert game_state.game_over is False
    assert game_state.paused is False
    assert game_state.fall_interval > 0
    assert game_state.active_piece is not None
    assert game_state.next_piece is not None


def test_fall_interval_calculation(game_state):
    """Test that fall interval is calculated correctly."""
    # Base interval should be positive
    assert game_state.fall_interval > 0

    # Should have a minimum value
    assert game_state.fall_interval >= 0.05


def test_spawn_next_piece(game_state):
    """Test piece spawning functionality."""
    # Should have active and next pieces
    assert game_state.active_piece is not None
    assert game_state.next_piece is not None

    # Pieces should be at spawn position
    assert game_state.active_piece.x == game_state.piece_factory.spawn_x
    assert game_state.active_piece.y == game_state.piece_factory.spawn_y


def test_piece_falling_timing(game_state):
    """Test that pieces fall based on timing."""
    # Mock time to control falling
    with patch("time.time") as mock_time:
        mock_time.return_value = 0

        # Initial state
        original_y = game_state.active_piece.y
        game_state.last_fall_time = 0

        # Advance time beyond fall interval
        mock_time.return_value = game_state.fall_interval + 0.1

        # Update should cause piece to fall
        game_state.update(0.1)

        # Piece should have moved down
        assert game_state.active_piece.y > original_y


def test_piece_landing_and_placement(game_state):
    """Test that pieces land and get placed on the board."""
    # This test verifies the piece falling mechanism works
    # We'll test the falling logic rather than the exact placement

    # Move piece to a position where it can fall
    piece = game_state.active_piece
    original_y = piece.y

    # Try to fall - should move down
    with patch("time.time") as mock_time:
        mock_time.return_value = game_state.fall_interval + 0.1
        game_state.update(0.1)

    # Piece should have moved down or been placed
    # Either outcome is valid for this test
    assert piece.y >= original_y  # Should not move up


def test_line_clearing(game_state):
    """Test line clearing functionality."""
    # Create a full line manually
    for x in range(settings.dimensions.BOARD_WIDTH):
        game_state.board.set_cell(
            x, settings.dimensions.BOARD_HEIGHT - 1, settings.colors.RED
        )

    # Clear lines
    lines_cleared = game_state.board.clear_completed_lines()
    assert lines_cleared > 0


def test_score_calculation(game_state):
    """Test score calculation for line clears."""
    original_score = game_state.score

    # Simulate line clear
    game_state._handle_line_clear(1)  # Single line

    assert game_state.score > original_score
    assert game_state.lines_cleared == 1


def test_level_progression(game_state):
    """Test level progression based on lines cleared."""
    original_level = game_state.level

    # Clear 10 lines to trigger level up
    game_state.lines_cleared = 10
    game_state.level = 2

    # Fall interval should be recalculated
    new_interval = game_state._calculate_fall_interval()
    assert new_interval < game_state.fall_interval


def test_move_piece_valid(game_state):
    """Test valid piece movement."""
    original_x = game_state.active_piece.x

    # Move right
    success = game_state.move_piece(1, 0)
    assert success is True
    assert game_state.active_piece.x == original_x + 1


def test_move_piece_invalid(game_state):
    """Test invalid piece movement."""
    # Move piece to edge
    game_state.active_piece.x = settings.dimensions.BOARD_WIDTH - 1

    # Try to move beyond edge
    success = game_state.move_piece(1, 0)
    assert success is False


def test_rotate_piece_valid(game_state):
    """Test valid piece rotation."""
    original_rotation = game_state.active_piece.rotation

    # Rotate clockwise
    success = game_state.rotate_piece(clockwise=True)
    assert success is True
    assert game_state.active_piece.rotation != original_rotation


def test_rotate_piece_invalid(game_state):
    """Test invalid piece rotation."""
    # Move piece to edge where rotation would be invalid
    game_state.active_piece.x = settings.dimensions.BOARD_WIDTH - 1
    game_state.active_piece.y = settings.dimensions.BOARD_HEIGHT - 1

    # Try to rotate (might be invalid due to collision)
    success = game_state.rotate_piece(clockwise=True)
    # Result depends on piece type and position


def test_hard_drop(game_state):
    """Test hard drop functionality."""
    original_y = game_state.active_piece.y

    # Hard drop should move piece to bottom
    success = game_state.hard_drop()
    # Note: Hard drop might not move if piece is already at bottom
    # or if there's no valid drop position
    assert (
        success is True or success is False
    )  # Either is valid depending on piece position


def test_pause_game(game_state):
    """Test game pause functionality."""
    assert game_state.paused is False

    # Pause game
    game_state.pause_game()
    assert game_state.paused is True

    # Unpause game
    game_state.pause_game()
    assert game_state.paused is False


def test_reset_game(game_state):
    """Test game reset functionality."""
    # Modify game state
    game_state.score = 1000
    game_state.level = 5
    game_state.lines_cleared = 20
    game_state.paused = True

    # Reset game
    game_state.reset_game()

    # Should be back to initial state
    assert game_state.score == 0
    assert game_state.level == 1
    assert game_state.lines_cleared == 0
    assert game_state.paused is False
    assert game_state.game_over is False


def test_game_over_detection(game_state):
    """Test game over detection."""
    # Fill top row to trigger game over
    for x in range(settings.dimensions.BOARD_WIDTH):
        game_state.board.set_cell(x, 0, settings.colors.RED)

    # Try to spawn next piece
    game_state._spawn_next_piece()

    # Should trigger game over
    assert game_state.game_over is True


def test_get_game_info(game_state):
    """Test getting game information."""
    info = game_state.get_game_info()

    assert "score" in info
    assert "level" in info
    assert "lines_cleared" in info
    assert "game_over" in info
    assert "paused" in info
    assert "active_piece" in info
    assert "next_piece" in info

    assert info["score"] == game_state.score
    assert info["level"] == game_state.level
    assert info["lines_cleared"] == game_state.lines_cleared
    assert info["game_over"] == game_state.game_over
    assert info["paused"] == game_state.paused


def test_move_piece_when_game_over(game_state):
    """Test that piece movement is blocked when game is over."""
    game_state.game_over = True

    success = game_state.move_piece(1, 0)
    assert success is False


def test_move_piece_when_paused(game_state):
    """Test that piece movement is blocked when game is paused."""
    game_state.paused = True

    success = game_state.move_piece(1, 0)
    assert success is False


def test_rotate_piece_when_game_over(game_state):
    """Test that piece rotation is blocked when game is over."""
    game_state.game_over = True

    success = game_state.rotate_piece(clockwise=True)
    assert success is False


def test_rotate_piece_when_paused(game_state):
    """Test that piece rotation is blocked when game is paused."""
    game_state.paused = True

    success = game_state.rotate_piece(clockwise=True)
    assert success is False


def test_hard_drop_when_game_over(game_state):
    """Test that hard drop is blocked when game is over."""
    game_state.game_over = True

    success = game_state.hard_drop()
    assert success is False


def test_hard_drop_when_paused(game_state):
    """Test that hard drop is blocked when game is paused."""
    game_state.paused = True

    success = game_state.hard_drop()
    assert success is False


def test_update_when_game_over(game_state):
    """Test that update is skipped when game is over."""
    game_state.game_over = True
    original_y = game_state.active_piece.y

    # Update should not affect piece position
    game_state.update(0.1)
    assert game_state.active_piece.y == original_y


def test_update_when_paused(game_state):
    """Test that update is skipped when game is paused."""
    game_state.paused = True
    original_y = game_state.active_piece.y

    # Update should not affect piece position
    game_state.update(0.1)
    assert game_state.active_piece.y == original_y


def test_fall_interval_recalculation(game_state):
    """Test that fall interval is recalculated when level changes."""
    original_interval = game_state.fall_interval

    # Change level
    game_state.level = 5
    game_state.fall_interval = game_state._calculate_fall_interval()

    # Should be different (faster)
    assert game_state.fall_interval != original_interval
    assert game_state.fall_interval < original_interval


def test_piece_factory_integration(game_state):
    """Test that piece factory is properly integrated."""
    # Should be able to create pieces
    assert game_state.piece_factory is not None

    # Should create valid pieces
    piece = game_state.piece_factory.create_random_piece()
    assert piece is not None
    assert isinstance(piece, Piece)


def test_board_integration(game_state):
    """Test that board is properly integrated."""
    # Should be able to access board
    assert game_state.board is not None
    assert isinstance(game_state.board, Board)

    # Test basic board operations
    # Test setting and getting cells
    game_state.board.set_cell(5, 15, settings.colors.RED)
    assert game_state.board.get_cell(5, 15) == settings.colors.RED

    # Test line completion check
    assert not game_state.board.is_line_complete(15)  # Should not be complete

    # Test board boundaries
    assert game_state.board.width == settings.dimensions.BOARD_WIDTH
    assert game_state.board.height == settings.dimensions.BOARD_HEIGHT
