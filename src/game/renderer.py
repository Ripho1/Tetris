"""
Game Renderer System

This module handles all rendering operations including:
- Board rendering with grid and pieces
- Piece rendering (active and placed)
- UI elements (score, level, next piece)
- Visual effects and animations
"""

import pygame
from typing import Optional, Tuple
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

        Displays a small preview of the upcoming piece in a configurable location.
        The preview location can be set to any of the four corners of the screen
        via settings.renderer.NEXT_PIECE_LOCATION.

        Args:
            piece: The next piece to preview
        """
        if piece is None:
            return

        # Use configured absolute position (top-left of preview box)
        preview_x, preview_y = settings.renderer.NEXT_PREVIEW_POSITION

        # Draw "Next" label above the preview box for all locations
        next_label = self.font.render("Next:", True, settings.colors.WHITE)
        label_height = self.font.get_height()
        label_margin = settings.renderer.PREVIEW_LABEL_MARGIN

        # Always place label above the preview box
        label_y = preview_y - label_height - label_margin

        self.screen.blit(next_label, (preview_x, label_y))

        # Draw preview box background
        preview_box_size = settings.renderer.PREVIEW_BOX_SIZE
        preview_box = pygame.Rect(
            preview_x, preview_y, preview_box_size, preview_box_size
        )
        pygame.draw.rect(self.screen, settings.colors.GRAY, preview_box, 1)

        # Get piece cells (relative to piece position)
        piece_cells = piece.get_cells()

        if not piece_cells:
            return

        # Calculate bounding box of the piece to center it
        min_x = min(x for x, y in piece_cells)
        max_x = max(x for x, y in piece_cells)
        min_y = min(y for x, y in piece_cells)
        max_y = max(y for x, y in piece_cells)

        piece_width = max_x - min_x + 1
        piece_height = max_y - min_y + 1

        # Scale for preview (smaller cells)
        preview_cell_size = min(
            20, preview_box_size // max(piece_width, piece_height, 4)
        )

        # Calculate centering offset
        piece_pixel_width = piece_width * preview_cell_size
        piece_pixel_height = piece_height * preview_cell_size
        offset_x = preview_x + (preview_box_size - piece_pixel_width) // 2
        offset_y = preview_y + (preview_box_size - piece_pixel_height) // 2

        # Draw each cell of the piece
        for cell_x, cell_y in piece_cells:
            # Calculate position relative to piece bounds
            rel_x = cell_x - min_x
            rel_y = cell_y - min_y

            # Draw the cell
            cell_rect = pygame.Rect(
                offset_x + rel_x * preview_cell_size + 1,
                offset_y + rel_y * preview_cell_size + 1,
                preview_cell_size - 2,
                preview_cell_size - 2,
            )
            pygame.draw.rect(self.screen, piece.color, cell_rect)

    def render_game_over(self, final_score: int):
        """
        Render the game over screen.

        Displays a semi-transparent overlay with "GAME OVER" message,
        final score, and instructions to restart or quit.

        Args:
            final_score: The final score achieved
        """
        # Create semi-transparent overlay
        overlay = pygame.Surface(
            (settings.dimensions.SCREEN_WIDTH, settings.dimensions.SCREEN_HEIGHT)
        )
        overlay.set_alpha(180)  # Semi-transparent (0=transparent, 255=opaque)
        overlay.fill(settings.colors.BLACK)
        self.screen.blit(overlay, (0, 0))

        # Render "GAME OVER" text
        game_over_text = self.large_font.render("GAME OVER", True, settings.colors.RED)
        game_over_rect = game_over_text.get_rect(
            center=(
                settings.dimensions.SCREEN_WIDTH // 2,
                settings.dimensions.SCREEN_HEIGHT // 2 - 60,
            )
        )
        self.screen.blit(game_over_text, game_over_rect)

        # Render final score
        score_text = self.font.render(
            f"Final Score: {final_score}", True, settings.colors.WHITE
        )
        score_rect = score_text.get_rect(
            center=(
                settings.dimensions.SCREEN_WIDTH // 2,
                settings.dimensions.SCREEN_HEIGHT // 2,
            )
        )
        self.screen.blit(score_text, score_rect)

        # Render restart instructions
        restart_text = self.font.render(
            "Press R to Restart", True, settings.colors.LIGHT_GRAY
        )
        restart_rect = restart_text.get_rect(
            center=(
                settings.dimensions.SCREEN_WIDTH // 2,
                settings.dimensions.SCREEN_HEIGHT // 2 + 40,
            )
        )
        self.screen.blit(restart_text, restart_rect)

        # Render quit instructions
        quit_text = self.font.render(
            "Press ESC to Quit", True, settings.colors.LIGHT_GRAY
        )
        quit_rect = quit_text.get_rect(
            center=(
                settings.dimensions.SCREEN_WIDTH // 2,
                settings.dimensions.SCREEN_HEIGHT // 2 + 70,
            )
        )
        self.screen.blit(quit_text, quit_rect)

    def clear_screen(self):
        """
        Clear the entire screen with black background.
        """
        self.screen.fill(settings.colors.BLACK)
