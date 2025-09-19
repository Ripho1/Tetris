"""
Game Board System

This module manages the Tetris game board including:
- Board state (empty/filled cells)
- Line detection and clearing
- Collision detection
- Board rendering data
"""

from typing import List, Tuple, Optional
from src.config.settings import settings
from src.game.piece import Piece


class Board:
    """
    Represents the Tetris game board (playing field).

    Manages:
    - 10x20 grid of cells (standard Tetris dimensions)
    - Cell states (empty or filled with color)
    - Line clearing logic
    - Collision detection
    """

    def __init__(self):
        """
        Initialize an empty game board.

        Creates a 10x20 (default Tetris dimensions) grid with all cells empty.
        """
        self.width = settings.dimensions.BOARD_WIDTH
        self.height = settings.dimensions.BOARD_HEIGHT

        # Board grid: None = empty, tuple = filled with color
        self.grid: List[List[Optional[Tuple[int, int, int]]]] = []
        self._initialize_grid()

    def _initialize_grid(self):
        """
        Create an empty board grid.

        Initializes all cells to None (empty).
        """
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]

    def is_valid_position(self, piece: Piece, dx: int = 0, dy: int = 0) -> bool:
        """
        Check if a piece can be placed at the given position.

        Args:
            piece: The piece to check
            dx: Horizontal offset from piece's current position
            dy: Vertical offset from piece's current position

        Returns:
            True if position is valid, False otherwise

        Checks for:
        - Board boundaries
        - Collision with existing pieces

        TODO: Implement collision detection logic.
        """
        # Test position would be piece.x + dx, piece.y + dy
        # Get all cells the piece would occupy
        # Check each cell is within bounds and empty
        pass

    def place_piece(self, piece: Piece):
        """
        Permanently place a piece on the board.

        Args:
            piece: The piece to place

        Sets the board cells to the piece's color.
        Should only be called after validating position.

        TODO: Implement piece placement logic.
        """
        # Get all cells the piece occupies
        # Set those board cells to the piece's color
        pass

    def clear_completed_lines(self) -> int:
        """
        Remove all completed lines from the board.

        Returns:
            Number of lines cleared

        A line is complete when all cells in a row are filled.
        After clearing, rows above fall down to fill the gaps.

        TODO: Implement line detection and clearing.
        """
        # Find all complete rows (no None values)
        # Remove complete rows
        # Add empty rows at the top
        # Return count of cleared lines
        pass

    def is_line_complete(self, row: int) -> bool:
        """
        Check if a specific row is completely filled.

        Args:
            row: Row index to check

        Returns:
            True if row is complete, False otherwise
        """
        return all(cell is not None for cell in self.grid[row])

    def get_cell(self, x: int, y: int) -> Optional[Tuple[int, int, int]]:
        """
        Get the color of a specific cell.

        Args:
            x: Column index
            y: Row index

        Returns:
            RGB color tuple if cell is filled, None if empty
            Returns None for out-of-bounds coordinates
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def set_cell(self, x: int, y: int, color: Optional[Tuple[int, int, int]]):
        """
        Set the color of a specific cell.

        Args:
            x: Column index
            y: Row index
            color: RGB color tuple or None for empty
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = color

    def is_game_over(self) -> bool:
        """
        Check if the game is over.

        Returns:
            True if pieces have reached the top of the board

        Game over occurs when the spawn area is blocked.
        TODO: Implement game over detection.
        """
        # Check if top rows have any filled cells
        # indicating pieces have stacked too high
        pass

    def clear_board(self):
        """
        Clear the entire board.

        Resets all cells to empty state.
        Useful for restarting or debug mode.
        """
        self._initialize_grid()
