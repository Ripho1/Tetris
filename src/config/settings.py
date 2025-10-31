"""
Game Settings and Configuration

This module contains all game constants and configuration values.
Centralizing these makes it easy to adjust game parameters.
Settings are organized into logical groups using classes as namespaces.
"""

import pygame


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


class Renderer:
    """Constants for the renderer system."""

    # Font sizes
    FONT_SIZE = 24
    LARGE_FONT_SIZE = 36

    # UI margins and spacing
    TOP_MARGIN = 50
    SIDE_PANEL_WIDTH = 200
    BOTTOM_MARGIN = 100

    # Cell sizing
    MAX_CELL_SIZE = 30
    CELL_PADDING = 1  # Space between cells and border

    # UI element positions
    SCORE_POSITION = (10, 10)
    LEVEL_POSITION = (10, 40)
    LINES_POSITION = (10, 70)

    # Next piece preview settings
    PREVIEW_BOX_SIZE = 100  # Size of the preview box in pixels
    PREVIEW_MARGIN = 20  # Margin from screen edges
    PREVIEW_LABEL_MARGIN = 8  # Spacing between label and preview box

    # Next piece preview absolute position (top-left of preview box)
    # Default: top-right corner with margins
    NEXT_PREVIEW_POSITION = (
        Dimensions.SCREEN_WIDTH - PREVIEW_BOX_SIZE - PREVIEW_MARGIN,
        FONT_SIZE + PREVIEW_LABEL_MARGIN,
    )


class Gameplay:
    """Constants for gameplay mechanics."""

    # Speed and timing
    BASE_FALL_INTERVAL = 1.0  # Base time between piece falls (seconds)
    SPEED_INCREASE_FACTOR = 0.1  # Speed increase per level (seconds)
    MIN_FALL_INTERVAL = 0.05  # Minimum fall interval (seconds)

    # Scoring system
    SCORE_SINGLE_LINE = 100
    SCORE_DOUBLE_LINE = 300
    SCORE_TRIPLE_LINE = 500
    SCORE_TETRIS = 800

    # Level progression
    LINES_PER_LEVEL = 10  # Lines needed to advance to next level


class Input:
    """Constants for input handling."""

    # Movement keys
    MOVE_LEFT_KEYS = [pygame.K_LEFT, pygame.K_a]
    MOVE_RIGHT_KEYS = [pygame.K_RIGHT, pygame.K_d]
    SOFT_DROP_KEYS = [pygame.K_DOWN, pygame.K_s]
    HARD_DROP_KEYS = [pygame.K_SPACE]

    # Rotation keys
    ROTATE_CLOCKWISE_KEYS = [pygame.K_UP, pygame.K_w]
    ROTATE_COUNTERCLOCKWISE_KEYS = [pygame.K_z]

    # Game control keys
    PAUSE_KEYS = [pygame.K_p]
    RESET_KEYS = [pygame.K_r]
    QUIT_KEYS = [pygame.K_ESCAPE]

    # Debug keys
    DEBUG_TOGGLE_KEYS = [pygame.K_F1]
    DEBUG_STEP_KEYS = [pygame.K_F2]
    DEBUG_CYCLE_PIECE_KEYS = [pygame.K_F3]
    DEBUG_CLEAR_ROW_KEYS = [pygame.K_l, pygame.K_DELETE]
    # Row selection uses existing arrows; handled only in paused+debug
    DEBUG_SELECT_ROW_UP_KEYS = [pygame.K_UP]
    DEBUG_SELECT_ROW_DOWN_KEYS = [pygame.K_DOWN]


# Create settings object with nested configuration
class Settings:
    """Main settings object that contains all configuration groups."""

    dimensions = Dimensions()
    colors = Colors()
    game = Game()
    renderer = Renderer()
    gameplay = Gameplay()
    input = Input()


# Create a global settings instance for easy access
settings = Settings()
