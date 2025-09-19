"""
Piece Factory

This module handles the creation and management of Tetrimino pieces.
Includes random piece generation and piece spawning logic.
"""

import random
from typing import Optional
from src.game.piece import Piece, PieceType
from src.config.settings import settings


class PieceFactory:
    """
    Factory class for creating Tetrimino pieces.

    Handles:
    - Random piece generation
    - Piece spawning at correct positions
    - Next piece preview functionality
    """

    def __init__(self):
        """
        Initialize the piece factory.

        Sets up random generation and spawn position.
        """
        # Default spawn position (top center of board)
        self.spawn_x = round(settings.dimensions.BOARD_WIDTH / 2)
        self.spawn_y = 0

        # Store all piece types for random selection
        self.piece_types = list(PieceType)

        self.pieces_order = list(self.piece_types)
        self.pieces_order = random.shuffle(self.pieces_order)

    def create_random_piece(self) -> Piece:
        """
        Create a random Tetrimino piece.

        Returns:
            New Piece instance with random type at spawn position

        Uses 7-bag randomization for better distribution.
        """
        piece_type = self.pieces_order.pop(0)

        if len(self.pieces_order) == 0:
            self.pieces_order = list(self.piece_types)
            self.pieces_order = random.shuffle(self.pieces_order)

        return self.create_piece(piece_type)

    def create_piece(self, piece_type: PieceType) -> Piece:
        """
        Create a specific type of Tetrimino piece.

        Args:
            piece_type: The type of piece to create

        Returns:
            New Piece instance at spawn position
        """
        return Piece(piece_type, self.spawn_x, self.spawn_y)

    def create_all_pieces(self) -> list[Piece]:
        """
        Create one of each piece type for testing.

        Returns:
            List containing one piece of each type

        Useful for debug mode and testing.
        TODO: Implement this method.
        """
        # Create one piece of each type
        # Return them in a list
        pass
