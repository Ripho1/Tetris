"""
Tetris Game - Entry Point

This is the main entry point for the Tetris game.
Initializes the game and starts the main game loop.
"""

import pygame
import sys
from src.game.engine import GameEngine


def main():
    """
    Main function that initializes and runs the Tetris game.

    This function:
    - Initializes pygame
    - Creates the game engine
    - Starts the main game loop
    - Handles cleanup on exit
    """
    # Initialize pygame
    pygame.init()

    try:
        # Create and run the game
        game = GameEngine()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
    finally:
        # Clean up
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
