# Configuration Guide

This guide explains how to customize various aspects of the Tetris game through the configuration system.

## Overview

All game settings are centralized in `src/config/settings.py`. This file organizes configuration into logical groups:
- **Dimensions**: Screen and board size
- **Colors**: All game colors
- **Game**: General game settings (FPS, title)
- **Renderer**: Visual rendering settings
- **Gameplay**: Game mechanics (speed, scoring)
- **Input**: Keyboard controls

## Common Customizations

### Next Piece Preview Position

The next piece preview is positioned using absolute pixel coordinates.

**Configuration Setting**: `settings.renderer.NEXT_PREVIEW_POSITION`

**Type**: `(x, y)` tuple representing the top-left of the preview box.

**How to Change**:

1. Open `src/config/settings.py`
2. Find the `Renderer` class
3. Set `NEXT_PREVIEW_POSITION` to the desired `(x, y)` tuple:

```python
class Renderer:
    # ... other settings ...

    # Example: top-right corner (default)
    NEXT_PREVIEW_POSITION = (
        Dimensions.SCREEN_WIDTH - PREVIEW_BOX_SIZE - PREVIEW_MARGIN,
        FONT_SIZE + PREVIEW_LABEL_MARGIN,
    )
```



**Additional Preview Settings**:
```python
PREVIEW_BOX_SIZE = 100       # Size of the preview box (pixels)
PREVIEW_MARGIN = 20          # Distance from screen edges (pixels)
PREVIEW_LABEL_MARGIN = 8     # Spacing between label and preview box (pixels)
```

### Game Speed

Adjust how fast pieces fall at each level.

**Configuration Settings**:
- `settings.gameplay.BASE_FALL_INTERVAL` - Starting speed (1.0 seconds default)
- `settings.gameplay.SPEED_INCREASE_FACTOR` - Speed increase per level (0.1 seconds default)
- `settings.gameplay.MIN_FALL_INTERVAL` - Fastest possible speed (0.05 seconds default)

**Example**:
```python
class Gameplay:
    BASE_FALL_INTERVAL = 0.8  # Start faster
    SPEED_INCREASE_FACTOR = 0.15  # Increase speed more per level
    MIN_FALL_INTERVAL = 0.03  # Allow even faster gameplay
```

### Level Progression

Control how many lines are needed to advance levels.

**Configuration Setting**: `settings.gameplay.LINES_PER_LEVEL`

**Default**: 10 lines per level

**Example**:
```python
class Gameplay:
    LINES_PER_LEVEL = 5  # Level up every 5 lines (faster progression)
```

### Scoring System

Customize points awarded for line clears.

**Configuration Settings**:
```python
class Gameplay:
    SCORE_SINGLE_LINE = 100   # 1 line cleared
    SCORE_DOUBLE_LINE = 300   # 2 lines cleared
    SCORE_TRIPLE_LINE = 500   # 3 lines cleared
    SCORE_TETRIS = 800        # 4 lines cleared (Tetris!)
```

### Screen Resolution

Change the game window size.

**Configuration Settings**:
```python
class Dimensions:
    SCREEN_WIDTH = 800   # Window width in pixels
    SCREEN_HEIGHT = 600  # Window height in pixels
```

**Note**: The game board automatically scales to fit the window while maintaining proper proportions.

### Controls

Customize keyboard controls for all game actions.

**Configuration Settings**:
```python
class Input:
    # Movement
    MOVE_LEFT_KEYS = [pygame.K_LEFT, pygame.K_a]
    MOVE_RIGHT_KEYS = [pygame.K_RIGHT, pygame.K_d]
    SOFT_DROP_KEYS = [pygame.K_DOWN, pygame.K_s]
    HARD_DROP_KEYS = [pygame.K_SPACE]
    
    # Rotation
    ROTATE_CLOCKWISE_KEYS = [pygame.K_UP, pygame.K_w]
    ROTATE_COUNTERCLOCKWISE_KEYS = [pygame.K_z]
    
    # Game controls
    PAUSE_KEYS = [pygame.K_p]
    RESET_KEYS = [pygame.K_r]
    QUIT_KEYS = [pygame.K_ESCAPE]

    # Debug
    DEBUG_TOGGLE_KEYS = [pygame.K_F1]
    DEBUG_STEP_KEYS = [pygame.K_F2]
    DEBUG_CYCLE_PIECE_KEYS = [pygame.K_F3]
    DEBUG_CLEAR_ROW_KEYS = [pygame.K_l, pygame.K_DELETE]
    DEBUG_SELECT_ROW_UP_KEYS = [pygame.K_UP]
    DEBUG_SELECT_ROW_DOWN_KEYS = [pygame.K_DOWN]
```

### Debug Mode

Enable or disable debug mode at runtime with the configured toggle key (default F1). When enabled, an on-screen debug overlay shows runtime info (FPS, score/level/lines, fall interval, current/next pieces). Additional debug helpers:

- `DEBUG_STEP_KEYS` (default F2): advance one fall step (works while paused)
- `DEBUG_CYCLE_PIECE_KEYS` (default F3): switch the active piece to the next type at spawn if valid
- `DEBUG_SELECT_ROW_UP_KEYS`/`DEBUG_SELECT_ROW_DOWN_KEYS` (default Up/Down): select a row to clear (recommended while paused)
- `DEBUG_CLEAR_ROW_KEYS` (default L or Delete): clear the selected row (no scoring)
- Mouse left-click on a filled cell: clear that contiguous placed piece (no scoring)

You can change these bindings in the `Input` section above.

**Example - Add More Keys**:
```python
# Allow both WASD and arrow keys for all movements
MOVE_LEFT_KEYS = [pygame.K_LEFT, pygame.K_a, pygame.K_KP4]  # Add numpad 4
ROTATE_CLOCKWISE_KEYS = [pygame.K_UP, pygame.K_w, pygame.K_x]  # Add X key
```

### UI Element Positions

Adjust where score, level, and lines are displayed.

**Configuration Settings**:
```python
class Renderer:
    SCORE_POSITION = (10, 10)   # (x, y) in pixels
    LEVEL_POSITION = (10, 40)
    LINES_POSITION = (10, 70)
```

### Piece Colors

Customize the colors for each Tetrimino piece.

**Configuration Settings**:
```python
class Colors:
    # RGB color tuples (red, green, blue)
    CYAN = (0, 255, 255)      # I-piece
    YELLOW = (255, 255, 0)    # O-piece
    PURPLE = (128, 0, 128)    # T-piece
    GREEN = (0, 255, 0)       # S-piece
    RED = (255, 0, 0)         # Z-piece
    BLUE = (0, 0, 255)        # J-piece
    ORANGE = (255, 165, 0)    # L-piece
```

## Tips

1. **Test Changes**: After modifying settings, run the game to see the changes:
   ```bash
   python commands.py game
   ```

2. **Reset to Defaults**: Keep a backup of the original `settings.py` file if you want to revert changes.

3. **Consistent Style**: When changing colors or positions, maintain consistency for the best visual experience.

4. **Performance**: Extremely high speeds (very low fall intervals) may affect gameplay experience.

## Advanced Customization

For more advanced customization beyond these settings, you may need to modify the source code in:
- `src/game/game_state.py` - Game logic
- `src/game/renderer.py` - Visual rendering
- `src/game/engine.py` - Game loop and controls

Always follow the coding standards defined in the `cursor-rules/` directory when making custom changes.

