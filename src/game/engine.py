"""
Game Engine - Main Game Loop and State Management

This class manages the core game loop, handles events, and coordinates
all game systems. It serves as the central controller for the Tetris game.
"""

import pygame
from src.config.settings import settings


class GameEngine:
    """
    Main game engine that handles the game loop and core systems.

    This class is responsible for:
    - Creating and managing the game window
    - Running the main game loop
    - Handling basic events (quit, etc.)
    - Managing the frame rate
    """

    def __init__(self):
        """
        Initialize the game engine.

        Sets up the display, clock, and initial game state.
        """
        # Create the game window
        self.screen = pygame.display.set_mode(
            (settings.dimensions.SCREEN_WIDTH, settings.dimensions.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(settings.game.WINDOW_TITLE)

        # Create clock for controlling frame rate
        self.clock = pygame.time.Clock()

        # Game state
        self.running = True

    def handle_events(self):
        """
        Handle pygame events.

        Currently handles:
        - Quit events (window close, ESC key)

        This method will be expanded later to handle game controls.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        """
        Update game state.

        Currently placeholder - will contain game logic updates
        like piece movement, collision detection, etc.
        """
        pass

    def render(self):
        """
        Render the game to the screen.

        Currently just clears the screen with black background.
        Later will render the game board, pieces, UI, etc.
        """
        # Clear screen with black background
        self.screen.fill(settings.colors.BLACK)

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
