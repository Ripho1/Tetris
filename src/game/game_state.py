"""
Game State Management

This module manages the overall game state including:
- Active piece management
- Piece falling mechanics
- Game progression (score, level, lines)
- Game over detection
"""

from typing import Optional, Dict, Tuple, List
from src.game.board import Board
from src.game.piece import Piece, PieceType
from src.game.piece_factory import PieceFactory
from src.config.settings import settings


class GameState:
    """
    Manages the overall state of the Tetris game.

    This class handles:
    - Active piece management and falling
    - Game progression (score, level, lines)
    - Piece spawning and placement
    - Game over detection
    """

    def __init__(self):
        """
        Initialize the game state.

        Creates a new board, piece factory, and initializes game variables.
        """
        self.board = Board()
        self.piece_factory = PieceFactory()

        # Game state variables
        self.active_piece: Optional[Piece] = None
        self.next_piece: Optional[Piece] = None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0

        # Timing for piece falling (accumulates delta_time from engine)
        self.fall_interval = self._calculate_fall_interval()
        self._fall_timer = 0.0

        # Game state flags
        self.game_over = False
        self.paused = False
        self.debug_mode: bool = False
        self.debug_selected_row: Optional[int] = None

        # Spawn the first piece
        self._spawn_next_piece()

    def _calculate_fall_interval(self) -> float:
        """
        Calculate the fall interval based on current level.

        The fall interval determines how fast pieces drop. Each level increases
        the speed by reducing the interval between automatic piece falls.
        The interval has a minimum value to prevent impossibly fast gameplay.

        Returns:
            Time in seconds between piece falls

        Formula:
            interval = BASE_FALL_INTERVAL - (level - 1) * SPEED_INCREASE_FACTOR
            Capped at MIN_FALL_INTERVAL for playability
        """
        base_interval = settings.gameplay.BASE_FALL_INTERVAL
        speed_increase = (self.level - 1) * settings.gameplay.SPEED_INCREASE_FACTOR
        return max(settings.gameplay.MIN_FALL_INTERVAL, base_interval - speed_increase)

    def _spawn_next_piece(self):
        """
        Spawn the next piece and prepare the following one.

        Creates a new active piece and generates the next piece for preview.
        """
        if self.next_piece is None:
            # First piece - generate both active and next
            self.active_piece = self.piece_factory.create_random_piece()
            self.next_piece = self.piece_factory.create_random_piece()
        else:
            # Use the prepared next piece
            self.active_piece = self.next_piece
            self.next_piece = self.piece_factory.create_random_piece()

        # Check for immediate game over
        if not self.board.is_valid_position(self.active_piece):
            self.game_over = True

    def update(self, delta_time: float):
        """
        Update the game state.

        Args:
            delta_time: Time elapsed since last update in seconds

        Handles:
        - Piece falling based on timing
        - Collision detection
        - Line clearing
        - Level progression
        """
        if self.game_over or self.paused:
            return

        # Accumulate elapsed time and fall piece at intervals
        self._fall_timer += max(0.0, float(delta_time))
        while (
            self._fall_timer >= self.fall_interval
            and not self.game_over
            and not self.paused
        ):
            self._fall_piece()
            self._fall_timer -= self.fall_interval

    def _fall_piece(self):
        """
        Make the active piece fall one cell down.

        Handles collision detection and piece placement when landing.
        """
        if self.active_piece is None:
            return

        # Try to move the piece down
        if self.board.is_valid_position(self.active_piece, dy=1):
            self.active_piece.move(0, 1)
        else:
            # Piece has landed - place it on the board
            self._place_piece()

    def _place_piece(self):
        """
        Place the active piece on the board and handle line clearing.
        """
        if self.active_piece is None:
            return

        # Place the piece on the board
        self.board.place_piece(self.active_piece)

        # Clear completed lines
        lines_cleared = self.board.clear_completed_lines()
        if lines_cleared > 0:
            self._handle_line_clear(lines_cleared)

        # Spawn the next piece
        self._spawn_next_piece()

    def _handle_line_clear(self, lines_cleared: int):
        """
        Handle line clearing and update score/level.

        Args:
            lines_cleared: Number of lines cleared
        """
        # Update lines cleared counter
        self.lines_cleared += lines_cleared

        # Calculate score based on lines cleared
        score_multiplier = {
            1: settings.gameplay.SCORE_SINGLE_LINE,
            2: settings.gameplay.SCORE_DOUBLE_LINE,
            3: settings.gameplay.SCORE_TRIPLE_LINE,
            4: settings.gameplay.SCORE_TETRIS,
        }
        base_score = score_multiplier.get(
            lines_cleared, settings.gameplay.SCORE_SINGLE_LINE
        )
        level_bonus = self.level * base_score
        self.score += base_score + level_bonus

        # Check for level up
        new_level = (self.lines_cleared // settings.gameplay.LINES_PER_LEVEL) + 1
        if new_level > self.level:
            self.level = new_level
            self.fall_interval = self._calculate_fall_interval()

    def move_piece(self, dx: int, dy: int) -> bool:
        """
        Move the active piece horizontally or vertically.

        Args:
            dx: Horizontal movement (positive = right)
            dy: Vertical movement (positive = down)

        Returns:
            True if movement was successful, False otherwise
        """
        if self.active_piece is None or self.game_over or self.paused:
            return False

        # Check if the new position is valid
        if self.board.is_valid_position(self.active_piece, dx, dy):
            self.active_piece.move(dx, dy)
            return True

        return False

    def rotate_piece(self, clockwise: bool = True) -> bool:
        """
        Rotate the active piece.

        Args:
            clockwise: True for clockwise rotation, False for counterclockwise

        Returns:
            True if rotation was successful, False otherwise
        """
        if self.active_piece is None or self.game_over or self.paused:
            return False

        # Create a copy to test rotation
        test_piece = self.active_piece.copy()

        # Apply rotation
        if clockwise:
            test_piece.rotate_clockwise()
        else:
            test_piece.rotate_counterclockwise()

        # Check if the rotated position is valid
        if self.board.is_valid_position(test_piece):
            # Apply rotation to actual piece
            if clockwise:
                self.active_piece.rotate_clockwise()
            else:
                self.active_piece.rotate_counterclockwise()
            return True

        return False

    def hard_drop(self) -> bool:
        """
        Instantly drop the active piece to the bottom.

        Returns:
            True if drop was successful, False otherwise
        """
        if self.active_piece is None or self.game_over or self.paused:
            return False

        # Find the lowest valid position
        drop_distance = 0
        while self.board.is_valid_position(self.active_piece, dy=drop_distance + 1):
            drop_distance += 1

        # Move if possible, then always place the piece
        if drop_distance > 0:
            self.active_piece.move(0, drop_distance)

        self._place_piece()
        return True

    def pause_game(self):
        """
        Toggle game pause state.
        """
        self.paused = not self.paused

    def reset_game(self):
        """
        Reset the game to initial state.
        """
        self.board.clear_board()
        self.active_piece = None
        self.next_piece = None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.paused = False
        self.fall_interval = self._calculate_fall_interval()
        self._fall_timer = 0.0
        self._spawn_next_piece()

    def get_game_info(self) -> dict:
        """
        Get current game information.

        Returns:
            Dictionary containing current game state
        """
        return {
            "score": self.score,
            "level": self.level,
            "lines_cleared": self.lines_cleared,
            "game_over": self.game_over,
            "paused": self.paused,
            "active_piece": self.active_piece,
            "next_piece": self.next_piece,
        }

    # -------------------- Debug helpers --------------------
    def get_debug_info(self) -> Dict[str, object]:
        """
        Collect debug information for on-screen display.

        Returns:
            Dictionary with key runtime values useful for debugging.
        """
        active_type = (
            self.active_piece.piece_type.value
            if self.active_piece is not None
            else None
        )
        next_type = (
            self.next_piece.piece_type.value if self.next_piece is not None else None
        )
        active_pos: Tuple[int, int] | None = (
            (self.active_piece.x, self.active_piece.y) if self.active_piece else None
        )
        active_rot = self.active_piece.rotation if self.active_piece else None

        return {
            "debug_mode": self.debug_mode,
            "score": self.score,
            "level": self.level,
            "lines_cleared": self.lines_cleared,
            "fall_interval": self.fall_interval,
            "game_over": self.game_over,
            "paused": self.paused,
            "active_type": active_type,
            "active_pos": active_pos,
            "active_rotation": active_rot,
            "next_type": next_type,
            "board_size": (self.board.width, self.board.height),
            "selected_row": self.debug_selected_row,
        }

    def debug_step_fall(self) -> bool:
        """
        Advance a single fall step regardless of pause state.

        Returns:
            True if a step occurred, False otherwise.
        """
        if self.game_over or self.active_piece is None:
            return False

        # Perform one fall attempt without using timers
        if self.board.is_valid_position(self.active_piece, dy=1):
            self.active_piece.move(0, 1)
        else:
            self._place_piece()
        return True

    def debug_cycle_active_piece(self) -> bool:
        """
        Cycle the active piece to the next type at spawn position.

        Returns:
            True if piece changed, False otherwise.
        """
        if self.game_over:
            return False

        piece_types = list(PieceType)

        # Determine next type
        if self.active_piece is None:
            next_type = piece_types[0]
        else:
            try:
                idx = piece_types.index(self.active_piece.piece_type)
                next_type = piece_types[(idx + 1) % len(piece_types)]
            except ValueError:
                next_type = piece_types[0]

        candidate = self.piece_factory.create_piece(next_type)

        # Only switch if valid at spawn to avoid unintended game over
        if self.board.is_valid_position(candidate):
            self.active_piece = candidate
            return True

        return False

    def debug_select_row(self, delta: int) -> int:
        """
        Select a board row for clearing by adjusting the current selection.

        Args:
            delta: Change in row index (negative moves up, positive moves down)

        Returns:
            The resulting selected row index.
        """
        if self.game_over:
            return -1

        max_row = self.board.height - 1
        if self.debug_selected_row is None:
            self.debug_selected_row = 0

        self.debug_selected_row = max(0, min(max_row, self.debug_selected_row + delta))
        return self.debug_selected_row

    def debug_clear_row(self) -> bool:
        """
        Clear all cells in the currently selected row.

        Returns:
            True if a row was cleared, False otherwise.
        Note:
            This does not affect scoring/lines and does not apply gravity.
        """
        if self.debug_selected_row is None or self.game_over:
            return False

        row = self.debug_selected_row
        for x in range(self.board.width):
            self.board.set_cell(x, row, None)
        return True

    def debug_clear_piece_at(self, x: int, y: int) -> bool:
        """
        Clear the contiguous placed piece region at board coordinates (x, y).

        Returns:
            True if any cells were cleared, False otherwise.
        Note:
            Operates only on placed blocks (board grid), not the active piece.
        """
        if self.game_over:
            return False

        target_color = self.board.get_cell(x, y)
        if target_color is None:
            return False

        width = self.board.width
        height = self.board.height

        stack: List[Tuple[int, int]] = [(x, y)]
        visited = set()
        cleared = 0

        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))

            if not (0 <= cx < width and 0 <= cy < height):
                continue

            if self.board.get_cell(cx, cy) != target_color:
                continue

            # Clear this cell
            self.board.set_cell(cx, cy, None)
            cleared += 1

            # Add neighbors (4-directional)
            stack.append((cx - 1, cy))
            stack.append((cx + 1, cy))
            stack.append((cx, cy - 1))
            stack.append((cx, cy + 1))

        return cleared > 0
