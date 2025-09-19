"""
Basic Setup Tests

Tests to verify the basic project structure and imports work correctly.
"""

import pygame


def test_pygame_import():
    """Test that pygame can be imported."""
    assert pygame is not None


def test_config_import():
    """Test that configuration can be imported."""
    from src.config.settings import settings

    assert settings.dimensions.SCREEN_WIDTH > 0
    assert settings.dimensions.SCREEN_HEIGHT > 0
    assert settings.game.FPS > 0


def test_settings_structure():
    """Test that the settings structure is organized correctly."""
    from src.config.settings import settings

    # Test that all sections exist
    assert hasattr(settings, "dimensions")
    assert hasattr(settings, "colors")
    assert hasattr(settings, "game")

    # Test dimensions section
    assert hasattr(settings.dimensions, "SCREEN_WIDTH")
    assert hasattr(settings.dimensions, "SCREEN_HEIGHT")
    assert hasattr(settings.dimensions, "BOARD_WIDTH")
    assert hasattr(settings.dimensions, "BOARD_HEIGHT")

    # Test colors section
    assert hasattr(settings.colors, "BLACK")
    assert hasattr(settings.colors, "WHITE")
    assert hasattr(settings.colors, "GRAY")
    assert hasattr(settings.colors, "LIGHT_GRAY")

    # Test game section
    assert hasattr(settings.game, "FPS")
    assert hasattr(settings.game, "WINDOW_TITLE")


def test_game_engine_import():
    """Test that the game engine can be imported."""
    from src.game.engine import GameEngine

    assert GameEngine is not None


def test_game_engine_creation():
    """Test that the game engine can be created (without running)."""
    # Initialize pygame first
    pygame.init()

    try:
        from src.game.engine import GameEngine

        engine = GameEngine()
        assert engine is not None
        assert hasattr(engine, "screen")
        assert hasattr(engine, "clock")
        assert hasattr(engine, "running")
    finally:
        # Clean up
        pygame.quit()
