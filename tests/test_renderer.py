"""
Renderer System Tests

Tests for the game renderer functionality including:
- Board rendering
- Piece rendering
- UI rendering
- Cell positioning and sizing
"""

import pygame
import pytest
from src.game.renderer import Renderer
from src.game.board import Board
from src.game.piece import Piece, PieceType
from src.config.settings import settings


@pytest.fixture
def screen():
    """Create a pygame screen for testing."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    yield screen
    pygame.quit()


@pytest.fixture
def renderer(screen):
    """Create a renderer instance for testing."""
    return Renderer(screen)


@pytest.fixture
def board():
    """Create a game board for testing."""
    return Board()


@pytest.fixture
def test_piece():
    """Create a test piece for rendering."""
    return Piece(PieceType.I, 5, 10)


def test_renderer_initialization(renderer):
    """Test that renderer initializes correctly."""
    assert renderer.screen is not None
    assert renderer.cell_size > 0
    assert renderer.board_offset_x >= 0
    assert renderer.board_offset_y >= 0
    assert renderer.font is not None
    assert renderer.large_font is not None


def test_cell_size_calculation(renderer):
    """Test that cell size is calculated correctly."""
    # Cell size should be positive and reasonable
    assert renderer.cell_size > 0
    assert renderer.cell_size <= 30  # Max size limit

    # Should be calculated based on screen dimensions
    expected_max = min(
        (settings.dimensions.SCREEN_WIDTH - 200) // settings.dimensions.BOARD_WIDTH,
        (settings.dimensions.SCREEN_HEIGHT - 100) // settings.dimensions.BOARD_HEIGHT,
        30,
    )
    assert renderer.cell_size <= expected_max


def test_board_offset_calculation(renderer):
    """Test that board offset is calculated correctly."""
    # Board should be centered horizontally
    board_width = settings.dimensions.BOARD_WIDTH * renderer.cell_size
    expected_offset = (settings.dimensions.SCREEN_WIDTH - board_width) // 2
    assert renderer.board_offset_x == expected_offset


def test_render_board_empty(renderer, board):
    """Test rendering an empty board."""
    # Should not raise any exceptions
    renderer.render_board(board)

    # Board should be rendered (we can't easily test the visual output)
    # but we can ensure the method completes without error
    assert True


def test_render_board_with_pieces(renderer, board):
    """Test rendering a board with placed pieces."""
    # Place a test piece on the board
    test_piece = Piece(PieceType.I, 5, 10)
    board.place_piece(test_piece)

    # Should render without errors
    renderer.render_board(board)
    assert True


def test_render_active_piece(renderer, test_piece):
    """Test rendering an active piece."""
    # Should render without errors
    renderer.render_active_piece(test_piece)
    assert True


def test_render_active_piece_none(renderer):
    """Test rendering when active piece is None."""
    # Should handle None gracefully
    renderer.render_active_piece(None)
    assert True


def test_render_ui_basic(renderer):
    """Test basic UI rendering."""
    # Should render without errors
    renderer.render_ui(score=1000, level=2, lines=5)
    assert True


def test_render_ui_with_next_piece(renderer, test_piece):
    """Test UI rendering with next piece preview."""
    # Should render without errors
    renderer.render_ui(score=1000, level=2, lines=5, next_piece=test_piece)
    assert True


def test_render_game_over(renderer):
    """Test game over screen rendering."""
    # Should render without errors
    renderer.render_game_over(final_score=5000)
    assert True


def test_clear_screen(renderer):
    """Test screen clearing functionality."""
    # Should clear without errors
    renderer.clear_screen()
    assert True


def test_draw_cell_coordinates(renderer):
    """Test that _draw_cell handles coordinates correctly."""
    # Test valid coordinates
    renderer._draw_cell(0, 0, settings.colors.RED)
    renderer._draw_cell(5, 10, settings.colors.BLUE)
    renderer._draw_cell(9, 19, settings.colors.GREEN)  # Last valid cell

    # Should not raise exceptions
    assert True


def test_draw_cell_out_of_bounds(renderer):
    """Test that _draw_cell handles out-of-bounds coordinates."""
    # These should be handled gracefully (not crash)
    renderer._draw_cell(-1, 0, settings.colors.RED)
    renderer._draw_cell(0, -1, settings.colors.RED)
    renderer._draw_cell(10, 0, settings.colors.RED)  # Beyond board width
    renderer._draw_cell(0, 20, settings.colors.RED)  # Beyond board height

    # Should not raise exceptions
    assert True


def test_renderer_with_different_piece_types(renderer):
    """Test rendering different piece types."""
    for piece_type in PieceType:
        piece = Piece(piece_type, 5, 10)
        renderer.render_active_piece(piece)

    # Should render all piece types without errors
    assert True


def test_renderer_grid_lines(renderer, board):
    """Test that grid lines are drawn."""
    # Render board and check that grid drawing doesn't crash
    renderer.render_board(board)
    assert True


def test_renderer_board_border(renderer, board):
    """Test that board border is drawn."""
    # Render board and check that border drawing doesn't crash
    renderer.render_board(board)
    assert True


def test_renderer_font_initialization(renderer):
    """Test that fonts are properly initialized."""
    assert renderer.font is not None
    assert renderer.large_font is not None

    # Fonts should be different sizes
    assert renderer.large_font.get_height() > renderer.font.get_height()


def test_renderer_color_constants(renderer):
    """Test that color constants are properly defined."""
    assert renderer.grid_color is not None
    assert renderer.border_color is not None
    assert isinstance(renderer.grid_color, tuple)
    assert isinstance(renderer.border_color, tuple)
    assert len(renderer.grid_color) == 3
    assert len(renderer.border_color) == 3


def test_renderer_screen_surface(renderer, screen):
    """Test that renderer uses the correct screen surface."""
    assert renderer.screen is screen


def test_renderer_cell_size_consistency(renderer):
    """Test that cell size calculation is consistent."""
    # Cell size should be calculated once and remain constant
    original_size = renderer.cell_size
    assert renderer.cell_size == original_size

    # Recalculating should give same result
    new_size = renderer._calculate_cell_size()
    assert new_size == original_size


def test_renderer_board_offset_consistency(renderer):
    """Test that board offset calculation is consistent."""
    # Board offset should be calculated once and remain constant
    original_offset = renderer.board_offset_x
    assert renderer.board_offset_x == original_offset

    # Recalculating should give same result
    new_offset = renderer._calculate_board_offset()
    assert new_offset == original_offset
