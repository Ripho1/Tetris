"""
Tetrimino Piece System

This module handles all Tetrimino (game piece) logic including:
- 7 different piece types (I, O, T, S, Z, J, L)
- Piece rotation and movement
- Shape definitions and colors
- Piece state management
"""

from enum import Enum
from typing import List, Tuple
from src.config.settings import settings


class PieceType(Enum):
    """
    Enumeration of all 7 Tetrimino piece types.

    Each piece type has a unique shape and rotation pattern.
    """

    I = "I"  # Straight line piece
    O = "O"  # Square piece
    T = "T"  # T-shaped piece
    S = "S"  # S-shaped piece (zigzag)
    Z = "Z"  # Z-shaped piece (reverse zigzag)
    J = "J"  # J-shaped piece
    L = "L"  # L-shaped piece


class Piece:
    """
    Represents a single Tetrimino piece with its shape, position, and rotation.

    This class manages:
    - Piece position on the board
    - Current rotation state (0-3)
    - Shape data for all rotations
    - Color information
    """

    def __init__(self, piece_type: PieceType, x: int = 0, y: int = 0):
        """
        Initialize a new Tetrimino piece.

        Args:
            piece_type: The type of piece (I, O, T, S, Z, J, L)
            x: Starting X position (column)
            y: Starting Y position (row)
        """
        self.piece_type = piece_type
        self.x = x
        self.y = y
        self.rotation = 0  # Current rotation (0-3)

        # Get shape data and color for this piece type
        self.shapes = self._get_piece_shapes()
        self.color = self._get_piece_color()

    def _get_piece_shapes(self) -> List[List[List[int]]]:
        """
        Get all rotation states for this piece type.

        Returns:
            List of 4 rotation states, each containing a 2D grid
            where 1 = filled cell, 0 = empty cell

        Note: This method is partially implemented.
        TODO: Complete shape definitions for all piece types.
        """
        # Shape definitions: each piece has 4 rotation states
        # Each state is a 2D grid where 1 = filled, 0 = empty

        if self.piece_type == PieceType.I:
            # I-piece: straight line (4 cells)
            horizontal = [[1, 1, 1, 1]]
            vertical = [[1], [1], [1], [1]]

            return [
                # Rotation 0: horizontal
                horizontal,
                # Rotation 1: vertical
                vertical,
                # Rotation 2: horizontal (same as 0)
                horizontal,
                # Rotation 3: vertical (same as 1)
                vertical,
            ]

        elif self.piece_type == PieceType.O:
            # O-piece: 2x2 square (doesn't rotate)
            square = [[1, 1], [1, 1]]
            return [square, square, square, square]

        elif self.piece_type == PieceType.T:
            # T-piece: T-shaped
            return [
                # Rotation 0: T pointing up
                [[0, 1, 0], [1, 1, 1]],
                # TODO: Implement remaining T-piece rotations
                # Rotation 1: T pointing right
                [[1, 0], [1, 1], [1, 0]],
                # Rotation 2: T pointing down
                [[1, 1, 1], [0, 1, 0]],
                # Rotation 3: T pointing left
                [[0, 1], [1, 1], [0, 1]],
            ]

        # TODO: Implement S, Z, J, L piece shapes
        # For now, return a placeholder
        else:
            placeholder = [[1, 1], [1, 1]]  # Temporary square shape
            return [placeholder, placeholder, placeholder, placeholder]

    def _get_piece_color(self) -> Tuple[int, int, int]:
        """
        Get the RGB color for this piece type.

        Returns:
            RGB tuple representing the piece color

        Note: Uses standard Tetris colors.
        """
        color_map = {
            PieceType.I: settings.colors.CYAN,  # I-piece
            PieceType.O: settings.colors.YELLOW,  # O-piece
            PieceType.T: settings.colors.PURPLE,  # T-piece
            PieceType.S: settings.colors.GREEN,  # S-piece
            PieceType.Z: settings.colors.RED,  # Z-piece
            PieceType.J: settings.colors.BLUE,  # J-piece
            PieceType.L: settings.colors.ORANGE,  # L-piece
        }
        return color_map.get(self.piece_type, settings.colors.WHITE)

    def get_current_shape(self) -> List[List[int]]:
        """
        Get the current shape based on rotation state.

        Returns:
            2D grid representing the current piece shape
        """
        return self.shapes[self.rotation]

    def rotate_clockwise(self):
        """
        Rotate the piece 90 degrees clockwise.

        Updates the rotation state (0-3 cycle).
        Note: Collision checking should be done before calling this.
        """
        self.rotation = (self.rotation + 1) % 4

    def rotate_counterclockwise(self):
        """
        Rotate the piece 90 degrees counterclockwise.

        Updates the rotation state (0-3 cycle).
        Note: Collision checking should be done before calling this.
        """
        self.rotation = (self.rotation - 1) % 4

    def move(self, dx: int, dy: int):
        """
        Move the piece by the specified offset.

        Args:
            dx: Horizontal movement (positive = right)
            dy: Vertical movement (positive = down)

        Note: Collision checking should be done before calling this.
        """
        self.x += dx
        self.y += dy

    def get_cells(self) -> List[Tuple[int, int]]:
        """
        Get all occupied cell positions for this piece.

        Returns:
            List of (x, y) tuples representing filled cells
            in board coordinates

        TODO: Implement this method to convert shape grid
        to absolute board positions.
        """
        # This method should iterate through the current shape
        # and return absolute board positions for all filled cells
        pass

    def copy(self) -> "Piece":
        """
        Create a copy of this piece.

        Returns:
            New Piece instance with same state

        Useful for testing moves without modifying the original piece.
        TODO: Implement deep copy functionality.
        """
        # Create a new piece with same type and position
        # Copy rotation state as well
        pass
