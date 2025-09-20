"""
Game Renderer System

This module handles all rendering operations including:
- Board rendering with grid and pieces
- Piece rendering (active and placed)
- UI elements (score, level, next piece)
- Visual effects and animations
"""

import pygame
from typing import Optional, List, Tuple
from src.config.settings import settings
from src.game.board import Board
from src.game.piece import Piece


class Renderer:
    """
    Handles all rendering operations for the Tetris game.

    This class manages:
    - Board and piece rendering
    - UI element display
    - Visual effects and animations
    - Screen management and scaling
    """

    def __init__(self, screen: pygame.Surface):
        """
        Initialize the renderer with a pygame screen surface.

        Args:
            screen: The pygame surface to render to
        """
        self.screen = screen
        self.cell_size = self._calculate_cell_size()
        self.board_offset_x = self._calculate_board_offset()
        self.board_offset_y = settings.renderer.TOP_MARGIN

        # Font for UI text
        self.font = pygame.font.Font(None, settings.renderer.FONT_SIZE)
        self.large_font = pygame.font.Font(None, settings.renderer.LARGE_FONT_SIZE)

        # Colors for grid lines and UI
        self.grid_color = settings.colors.GRAY
        self.border_color = settings.colors.WHITE

    def _calculate_cell_size(self) -> int:
        """
        Calculate the optimal cell size based on screen dimensions.

        Returns:
            Size of each cell in pixels
        """
        # Reserve space for UI elements
        available_width = (
            settings.dimensions.SCREEN_WIDTH - settings.renderer.SIDE_PANEL_WIDTH
        )
        available_height = (
            settings.dimensions.SCREEN_HEIGHT - settings.renderer.BOTTOM_MARGIN
        )

        # Calculate cell size to fit board
        cell_width = available_width // settings.dimensions.BOARD_WIDTH
        cell_height = available_height // settings.dimensions.BOARD_HEIGHT

        # Use the smaller dimension to maintain square cells
        return min(cell_width, cell_height, settings.renderer.MAX_CELL_SIZE)

    def _calculate_board_offset(self) -> int:
        """
        Calculate the horizontal offset to center the board.

        Returns:
            X offset for board positioning
        """
        board_width = settings.dimensions.BOARD_WIDTH * self.cell_size
        return (settings.dimensions.SCREEN_WIDTH - board_width) // 2

    def render_board(self, board: Board):
        """
        Render the game board with all placed pieces.

        Args:
            board: The game board to render
        """
        # Clear the board area
        board_rect = pygame.Rect(
            self.board_offset_x,
            self.board_offset_y,
            settings.dimensions.BOARD_WIDTH * self.cell_size,
            settings.dimensions.BOARD_HEIGHT * self.cell_size,
        )
        pygame.draw.rect(self.screen, settings.colors.BLACK, board_rect)

        # Draw grid lines
        self._draw_grid_lines()

        # Draw placed pieces
        self._draw_placed_pieces(board)

        # Draw board border
        pygame.draw.rect(self.screen, self.border_color, board_rect, 2)

    def _draw_grid_lines(self):
        """
        Draw the grid lines on the board.

        Draws vertical and horizontal lines to show cell boundaries.
        """
        # Vertical lines
        for x in range(settings.dimensions.BOARD_WIDTH + 1):
            start_x = self.board_offset_x + x * self.cell_size
            start_y = self.board_offset_y
            end_x = start_x
            end_y = (
                self.board_offset_y + settings.dimensions.BOARD_HEIGHT * self.cell_size
            )
            pygame.draw.line(
                self.screen, self.grid_color, (start_x, start_y), (end_x, end_y)
            )

        # Horizontal lines
        for y in range(settings.dimensions.BOARD_HEIGHT + 1):
            start_x = self.board_offset_x
            start_y = self.board_offset_y + y * self.cell_size
            end_x = (
                self.board_offset_x + settings.dimensions.BOARD_WIDTH * self.cell_size
            )
            end_y = start_y
            pygame.draw.line(
                self.screen, self.grid_color, (start_x, start_y), (end_x, end_y)
            )

    def _draw_placed_pieces(self, board: Board):
        """
        Draw all placed pieces on the board.

        Args:
            board: The game board containing placed pieces
        """
        for x in range(settings.dimensions.BOARD_WIDTH):
            for y in range(settings.dimensions.BOARD_HEIGHT):
                cell_color = board.get_cell(x, y)
                if cell_color is not None:
                    self._draw_cell(x, y, cell_color)

    def render_active_piece(self, piece: Piece):
        """
        Render the currently active falling piece.

        Args:
            piece: The active piece to render
        """
        if piece is None:
            return

        # Get all cells occupied by the piece
        cells = piece.get_cells()

        for x, y in cells:
            # Check if cell is within board bounds
            if (
                0 <= x < settings.dimensions.BOARD_WIDTH
                and 0 <= y < settings.dimensions.BOARD_HEIGHT
            ):
                self._draw_cell(x, y, piece.color)

    def _draw_cell(self, x: int, y: int, color: Tuple[int, int, int]):
        """
        Draw a single cell at the specified position.

        Args:
            x: Column index
            y: Row index
            color: RGB color tuple
        """
        cell_rect = pygame.Rect(
            self.board_offset_x + x * self.cell_size + settings.renderer.CELL_PADDING,
            self.board_offset_y + y * self.cell_size + settings.renderer.CELL_PADDING,
            self.cell_size - (settings.renderer.CELL_PADDING * 2),
            self.cell_size - (settings.renderer.CELL_PADDING * 2),
        )
        pygame.draw.rect(self.screen, color, cell_rect)

    def render_ui(
        self,
        score: int = 0,
        level: int = 1,
        lines: int = 0,
        next_piece: Optional[Piece] = None,
    ):
        """
        Render UI elements (score, level, next piece preview).

        Args:
            score: Current score
            level: Current level
            lines: Lines cleared
            next_piece: Next piece to preview (optional)
        """
        # Score display
        score_text = self.font.render(f"Score: {score}", True, settings.colors.WHITE)
        self.screen.blit(score_text, settings.renderer.SCORE_POSITION)

        # Level display
        level_text = self.font.render(f"Level: {level}", True, settings.colors.WHITE)
        self.screen.blit(level_text, settings.renderer.LEVEL_POSITION)

        # Lines display
        lines_text = self.font.render(f"Lines: {lines}", True, settings.colors.WHITE)
        self.screen.blit(lines_text, settings.renderer.LINES_POSITION)

        # Next piece preview
        if next_piece is not None:
            self._render_next_piece(next_piece)

    def _render_next_piece(self, piece: Piece):
        """
        Render the next piece preview.

        Args:
            piece: The next piece to preview
        """
        # TODO: Implement next piece preview rendering
        # This will show a small preview of the upcoming piece
        pass

    def render_game_over(self, final_score: int):
        """
        Render the game over screen.

        Args:
            final_score: The final score achieved
        """
        # TODO: Implement game over screen
        # This will show game over message and final score
        pass

    def clear_screen(self):
        """
        Clear the entire screen with black background.
        """
        self.screen.fill(settings.colors.BLACK)
