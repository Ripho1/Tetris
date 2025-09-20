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
        self.rotation = 0  # Current rotation (0-3 by default)

        # Get shape data and color for this piece type
        self.shapes = self._get_piece_shapes()
        self.color = self._get_piece_color()

    def _get_piece_shapes(self) -> List[List[List[int]]]:
        """
        Get all rotation states for this piece type.

        Returns:
            List of 4 rotation states at most, each containing a 2D grid
            where 1 = filled cell, 0 = empty cell
        """
        # Shape definitions: each piece has 4 rotation states at most
        # Each state is a 2D grid where 1 = filled, 0 = empty

        if self.piece_type == PieceType.I:
            # I-piece: straight line (4 cells)
            horizontal = [[1], [1], [1], [1]]
            vertical = [[1, 1, 1, 1]]

            return [horizontal, vertical]

        elif self.piece_type == PieceType.O:
            # O-piece: 2x2 square (doesn't rotate)
            square = [[1, 1], [1, 1]]
            return [square]

        elif self.piece_type == PieceType.T:
            # T-piece: T-shaped
            top = [[0, 1], [1, 1], [0, 1]]
            right = [[1, 1, 1], [0, 1, 0]]
            bottom = [[1, 0], [1, 1], [1, 0]]
            left = [[0, 1, 0], [1, 1, 1]]

            return [top, right, bottom, left]

        elif self.piece_type == PieceType.S:
            # S-piece: S-shaped
            top = [[1, 0], [1, 1], [0, 1]]
            right = [[0, 1, 1], [1, 1, 0]]

            return [top, right]

        elif self.piece_type == PieceType.Z:
            # Z-piece: Z-shaped
            top = [[0, 1], [1, 1], [1, 0]]
            right = [[1, 1, 0], [0, 1, 1]]

            return [top, right]

        elif self.piece_type == PieceType.J:
            # J-piece: J-shaped
            top = [[0, 0, 1], [1, 1, 1]]
            right = [[1, 1], [0, 1], [0, 1]]
            bottom = [[1, 1, 1], [1, 0, 0]]
            left = [[1, 0], [1, 0], [1, 1]]

            return [top, right, bottom, left]

        elif self.piece_type == PieceType.L:
            # L-piece: L-shaped
            top = [[1, 1, 1], [0, 0, 1]]
            right = [[1, 1], [1, 0], [1, 0]]
            bottom = [[1, 0, 0], [1, 1, 1]]
            left = [[0, 1], [0, 1], [1, 1]]

            return [top, right, bottom, left]

        else:
            raise ValueError(f"Invalid piece type: {self.piece_type}")

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

        Updates the rotation state (0-3 cycle by default).
        Note: Collision checking should be done before calling this.
        """
        self.rotation = (self.rotation + 1) % len(self.shapes)

    def rotate_counterclockwise(self):
        """
        Rotate the piece 90 degrees counterclockwise.

        Updates the rotation state (0-3 cycle by default).
        Note: Collision checking should be done before calling this.
        """
        self.rotation = (self.rotation - 1) % len(self.shapes)

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
            in board coordinates where x is column and y is row

        """
        result = []
        for col_idx, column in enumerate(self.get_current_shape()):
            for row_idx, cell in enumerate(column):
                if cell == 1:
                    result.append((self.x + col_idx, self.y + row_idx))
        return result

    def copy(self) -> "Piece":
        """
        Create a copy of this piece.

        Returns:
            New Piece instance with same state

        Useful for testing moves without modifying the original piece.
        """

        copy = Piece(self.piece_type, self.x, self.y)
        copy.rotation = self.rotation

        return copy
