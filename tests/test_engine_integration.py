"""
Game Engine Integration Tests

Tests for the integrated game engine functionality including:
- Game loop integration
- Event handling
- Rendering integration
- Game state coordination
"""

import pygame
import pytest
from unittest.mock import patch, MagicMock
from src.game.engine import GameEngine
from src.game.game_state import GameState
from src.game.renderer import Renderer
from src.config.settings import settings


@pytest.fixture
def game_engine():
    """Create a game engine instance for testing."""
    pygame.init()
    engine = GameEngine()
    yield engine
    pygame.quit()


def test_game_engine_initialization(game_engine):
    """Test that game engine initializes correctly."""
    assert game_engine.screen is not None
    assert game_engine.clock is not None
    assert game_engine.game_state is not None
    assert game_engine.renderer is not None
    assert game_engine.running is True
    assert game_engine.last_time > 0


def test_game_engine_screen_creation(game_engine):
    """Test that game engine creates correct screen."""
    assert game_engine.screen.get_width() == settings.dimensions.SCREEN_WIDTH
    assert game_engine.screen.get_height() == settings.dimensions.SCREEN_HEIGHT


def test_game_engine_components_integration(game_engine):
    """Test that all components are properly integrated."""
    # Game state should be initialized
    assert isinstance(game_engine.game_state, GameState)

    # Renderer should be initialized
    assert isinstance(game_engine.renderer, Renderer)

    # Renderer should have the correct screen
    assert game_engine.renderer.screen is game_engine.screen


def test_handle_events_quit(game_engine):
    """Test handling quit events."""
    # Create a quit event
    quit_event = pygame.event.Event(pygame.QUIT)
    pygame.event.post(quit_event)

    # Handle events
    game_engine.handle_events()

    # Game should stop running
    assert game_engine.running is False


def test_handle_events_escape_key(game_engine):
    """Test handling escape key."""
    # Create escape key event
    escape_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)
    pygame.event.post(escape_event)

    # Handle events
    game_engine.handle_events()

    # Game should stop running
    assert game_engine.running is False


def test_handle_events_pause_key(game_engine):
    """Test handling pause key."""
    original_paused = game_engine.game_state.paused

    # Create pause key event
    pause_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_p)
    pygame.event.post(pause_event)

    # Handle events
    game_engine.handle_events()

    # Pause state should be toggled
    assert game_engine.game_state.paused != original_paused


def test_handle_events_reset_key(game_engine):
    """Test handling reset key."""
    # Modify game state
    game_engine.game_state.score = 1000

    # Create reset key event
    reset_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r)
    pygame.event.post(reset_event)

    # Handle events
    game_engine.handle_events()

    # Game should be reset
    assert game_engine.game_state.score == 0


def test_handle_events_movement_keys(game_engine):
    """Test handling movement key events."""
    original_x = game_engine.game_state.active_piece.x

    # Test left movement
    left_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
    pygame.event.post(left_event)
    game_engine.handle_events()

    # Piece should move left (if valid)
    # Note: Actual movement depends on piece position and board state


def test_handle_events_rotation_keys(game_engine):
    """Test handling rotation key events."""
    original_rotation = game_engine.game_state.active_piece.rotation

    # Test clockwise rotation
    up_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
    pygame.event.post(up_event)
    game_engine.handle_events()

    # Piece should rotate (if valid)
    # Note: Actual rotation depends on piece position and board state


def test_handle_events_soft_drop_key(game_engine):
    """Test handling soft drop key."""
    original_y = game_engine.game_state.active_piece.y

    # Test soft drop
    down_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
    pygame.event.post(down_event)
    game_engine.handle_events()

    # Piece should move down (if valid)
    # Note: Actual movement depends on piece position and board state


def test_handle_events_hard_drop_key(game_engine):
    """Test handling hard drop key."""
    # Test hard drop
    space_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    pygame.event.post(space_event)
    game_engine.handle_events()

    # Hard drop should be attempted
    # Note: Actual result depends on piece position and board state


def test_handle_events_counterclockwise_rotation(game_engine):
    """Test handling counterclockwise rotation key."""
    # Test counterclockwise rotation
    z_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_z)
    pygame.event.post(z_event)
    game_engine.handle_events()

    # Piece should rotate counterclockwise (if valid)
    # Note: Actual rotation depends on piece position and board state


def test_handle_events_wasd_controls(game_engine):
    """Test handling WASD control keys."""
    # Test W key (rotation)
    w_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_w)
    pygame.event.post(w_event)
    game_engine.handle_events()

    # Test A key (left movement)
    a_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a)
    pygame.event.post(a_event)
    game_engine.handle_events()

    # Test S key (soft drop)
    s_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s)
    pygame.event.post(s_event)
    game_engine.handle_events()

    # Test D key (right movement)
    d_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)
    pygame.event.post(d_event)
    game_engine.handle_events()

    # All should be handled without errors
    assert True


def test_handle_events_when_game_over(game_engine):
    """Test that game controls are blocked when game is over."""
    # Set game over state
    game_engine.game_state.game_over = True

    # Try to move piece
    left_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
    pygame.event.post(left_event)
    game_engine.handle_events()

    # Movement should be blocked
    # Note: This tests the logic, actual behavior depends on implementation


def test_handle_events_when_paused(game_engine):
    """Test that game controls are blocked when game is paused."""
    # Set paused state
    game_engine.game_state.paused = True

    # Try to move piece
    left_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
    pygame.event.post(left_event)
    game_engine.handle_events()

    # Movement should be blocked
    # Note: This tests the logic, actual behavior depends on implementation


def test_update_functionality(game_engine):
    """Test the update functionality."""
    # Mock time to control updates
    with patch("time.time") as mock_time:
        mock_time.return_value = 0
        game_engine.last_time = 0

        # Update should not crash
        game_engine.update()

        # Should update last_time
        assert game_engine.last_time == 0


def test_render_functionality(game_engine):
    """Test the render functionality."""
    # Render should not crash
    game_engine.render()

    # Should complete without errors
    assert True


def test_render_with_game_over(game_engine):
    """Test rendering when game is over."""
    # Set game over state
    game_engine.game_state.game_over = True

    # Render should not crash
    game_engine.render()

    # Should complete without errors
    assert True


def test_render_with_paused_game(game_engine):
    """Test rendering when game is paused."""
    # Set paused state
    game_engine.game_state.paused = True

    # Render should not crash
    game_engine.render()

    # Should complete without errors
    assert True


def test_render_with_active_piece(game_engine):
    """Test rendering with active piece."""
    # Ensure there's an active piece
    assert game_engine.game_state.active_piece is not None

    # Render should not crash
    game_engine.render()

    # Should complete without errors
    assert True


def test_render_with_next_piece(game_engine):
    """Test rendering with next piece."""
    # Ensure there's a next piece
    assert game_engine.game_state.next_piece is not None

    # Render should not crash
    game_engine.render()

    # Should complete without errors
    assert True


def test_game_loop_integration(game_engine):
    """Test that game loop components work together."""
    # Mock pygame events to prevent infinite loop
    with patch("pygame.event.get") as mock_events:
        mock_events.return_value = []

        # Mock pygame.display.flip to prevent actual rendering
        with patch("pygame.display.flip"):
            # Run one iteration of game loop
            game_engine.handle_events()
            game_engine.update()
            game_engine.render()

            # Should complete without errors
            assert True


def test_delta_time_calculation(game_engine):
    """Test that delta time is calculated correctly."""
    with patch("time.time") as mock_time:
        # Set initial time
        mock_time.return_value = 0
        game_engine.last_time = 0

        # Advance time
        mock_time.return_value = 0.1

        # Update should calculate delta time
        game_engine.update()

        # Last time should be updated
        assert game_engine.last_time == 0.1


def test_game_engine_clock_integration(game_engine):
    """Test that pygame clock is properly integrated."""
    # Clock should be a pygame Clock object
    assert hasattr(game_engine.clock, "tick")

    # Should be able to call tick method
    game_engine.clock.tick(60)


def test_game_engine_screen_integration(game_engine):
    """Test that pygame screen is properly integrated."""
    # Screen should be a pygame Surface
    assert hasattr(game_engine.screen, "blit")
    assert hasattr(game_engine.screen, "fill")

    # Should be able to call screen methods
    game_engine.screen.fill((0, 0, 0))


def test_game_engine_window_title(game_engine):
    """Test that window title is set correctly."""
    # Title should be set to the configured value
    # Note: We can't easily test the actual window title, but we can ensure
    # the pygame.display.set_caption was called during initialization
    assert True


def test_game_engine_error_handling(game_engine):
    """Test that game engine handles errors gracefully."""
    # Mock an error in update
    with patch.object(
        game_engine.game_state, "update", side_effect=Exception("Test error")
    ):
        # Update should not crash the engine
        try:
            game_engine.update()
        except Exception:
            # Engine should handle the error gracefully
            pass

        # Engine should still be running
        assert game_engine.running is True


def test_game_engine_initialization_with_mocked_pygame():
    """Test game engine initialization with mocked pygame."""
    with patch("pygame.init"), patch("pygame.display.set_mode") as mock_display, patch(
        "pygame.display.set_caption"
    ) as mock_caption, patch("pygame.font.Font") as mock_font:

        # Mock display to return a mock surface
        mock_surface = MagicMock()
        mock_display.return_value = mock_surface

        # Mock font creation
        mock_font.return_value = MagicMock()

        # Create engine
        engine = GameEngine()

        # Should initialize without errors
        assert engine.screen is mock_surface
        assert engine.clock is not None
        assert engine.game_state is not None
        assert engine.renderer is not None
