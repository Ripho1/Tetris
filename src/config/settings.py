"""
Game Settings and Configuration

This module contains all game constants and configuration values.
Centralizing these makes it easy to adjust game parameters.
Settings are organized into logical groups using classes as namespaces.
"""


class Dimensions:
    """Screen and game area dimensions."""

    # Screen dimensions (standard Tetris proportions)
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Game area dimensions (10x20 standard Tetris board)
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 20


class Colors:
    """Color definitions (RGB values)."""

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (192, 192, 192)

    # Tetris piece colors (standard)
    CYAN = (0, 255, 255)  # I-piece
    YELLOW = (255, 255, 0)  # O-piece
    PURPLE = (128, 0, 128)  # T-piece
    GREEN = (0, 255, 0)  # S-piece
    RED = (255, 0, 0)  # Z-piece
    BLUE = (0, 0, 255)  # J-piece
    ORANGE = (255, 165, 0)  # L-piece


class Game:
    """General game settings."""

    FPS = 60
    WINDOW_TITLE = "Tetris"


# Create settings object with nested configuration
class Settings:
    """Main settings object that contains all configuration groups."""

    dimensions = Dimensions()
    colors = Colors()
    game = Game()


# Create a global settings instance for easy access
settings = Settings()
