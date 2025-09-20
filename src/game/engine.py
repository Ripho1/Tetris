"""
Game Engine - Main Game Loop and State Management

This class manages the core game loop, handles events, and coordinates
all game systems. It serves as the central controller for the Tetris game.
"""

import pygame
import time
from src.config.settings import settings
from src.game.game_state import GameState
from src.game.renderer import Renderer


class GameEngine:
    """
    Main game engine that handles the game loop and core systems.

    This class is responsible for:
    - Creating and managing the game window
    - Running the main game loop
    - Handling input events and controls
    - Managing the frame rate
    - Coordinating game state and rendering
    """

    def __init__(self):
        """
        Initialize the game engine.

        Sets up the display, clock, game state, and renderer.
        """
        # Create the game window
        self.screen = pygame.display.set_mode(
            (settings.dimensions.SCREEN_WIDTH, settings.dimensions.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(settings.game.WINDOW_TITLE)

        # Create clock for controlling frame rate
        self.clock = pygame.time.Clock()

        # Initialize game systems
        self.game_state = GameState()
        self.renderer = Renderer(self.screen)

        # Game state
        self.running = True
        self.last_time = time.time()

    def handle_events(self):
        """
        Handle pygame events and game controls.

        Handles:
        - Quit events (window close, ESC key)
        - Game controls (movement, rotation, pause)
        - Debug controls (if enabled)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._handle_key_press(event.key)

    def _handle_key_press(self, key):
        """
        Handle individual key press events.

        Args:
            key: The pygame key constant that was pressed
        """
        if key in settings.input.QUIT_KEYS:
            self.running = False
        elif key in settings.input.PAUSE_KEYS:
            # Pause/unpause game
            self.game_state.pause_game()
        elif key in settings.input.RESET_KEYS:
            # Reset game (for testing)
            self.game_state.reset_game()
        elif not self.game_state.game_over and not self.game_state.paused:
            # Game controls (only when playing)
            self._handle_game_controls(key)

    def _handle_game_controls(self, key):
        """
        Handle game control key presses.

        Args:
            key: The pygame key constant that was pressed
        """
        # Movement controls
        if key in settings.input.MOVE_LEFT_KEYS:
            self.game_state.move_piece(-1, 0)
        elif key in settings.input.MOVE_RIGHT_KEYS:
            self.game_state.move_piece(1, 0)
        elif key in settings.input.SOFT_DROP_KEYS:
            # Soft drop
            self.game_state.move_piece(0, 1)
        elif key in settings.input.HARD_DROP_KEYS:
            # Hard drop
            self.game_state.hard_drop()

        # Rotation controls
        elif key in settings.input.ROTATE_CLOCKWISE_KEYS:
            # Clockwise rotation
            self.game_state.rotate_piece(clockwise=True)
        elif key in settings.input.ROTATE_COUNTERCLOCKWISE_KEYS:
            # Counterclockwise rotation
            self.game_state.rotate_piece(clockwise=False)

    def update(self):
        """
        Update game state.

        Handles:
        - Game state updates (piece falling, collisions, etc.)
        - Delta time calculation for smooth updates
        """
        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time

        # Update game state
        self.game_state.update(delta_time)

    def render(self):
        """
        Render the game to the screen.

        Renders:
        - Game board with placed pieces
        - Active falling piece
        - UI elements (score, level, etc.)
        - Game over screen if applicable
        """
        # Clear screen
        self.renderer.clear_screen()

        # Render game board
        self.renderer.render_board(self.game_state.board)

        # Render active piece
        if self.game_state.active_piece is not None:
            self.renderer.render_active_piece(self.game_state.active_piece)

        # Render UI
        game_info = self.game_state.get_game_info()
        self.renderer.render_ui(
            score=game_info["score"],
            level=game_info["level"],
            lines=game_info["lines_cleared"],
            next_piece=game_info["next_piece"],
        )

        # Render game over screen if needed
        if self.game_state.game_over:
            self.renderer.render_game_over(game_info["score"])

        # Update the display
        pygame.display.flip()

    def run(self):
        """
        Main game loop.

        This is the heart of the game - it continuously:
        1. Handles user input
        2. Updates game state
        3. Renders the current frame
        4. Controls frame rate

        The loop continues until the game is quit.
        """
        print(
            f"Starting Tetris game - {settings.dimensions.SCREEN_WIDTH}x{settings.dimensions.SCREEN_HEIGHT} at {settings.game.FPS} FPS"
        )

        while self.running:
            # Handle events (input, window close, etc.)
            self.handle_events()

            # Update game state
            self.update()

            # Render current frame
            self.render()

            # Control frame rate
            self.clock.tick(settings.game.FPS)

        print("Game ended")
