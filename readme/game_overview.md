# Tetris Game Overview

## What is Tetris?

Tetris is a classic puzzle video game where players manipulate falling geometric shapes called "Tetriminos" to create complete horizontal lines. When a line is filled without gaps, it disappears, making room for more pieces. The game gets progressively faster and more challenging as you advance through levels.

## Core Game Mechanics

### The Playing Field (Matrix)
- **Dimensions**: 10 columns wide × 20 rows high
- **Purpose**: Confined space where all gameplay occurs
- **Visual**: Empty cells are typically black/dark, filled cells show the piece colors

### The Tetriminos (Game Pieces)
Seven distinct shapes, each made of 4 connected squares:

- **I-piece**: Straight line (4 squares in a row)
- **O-piece**: 2×2 square
- **T-piece**: T-shaped
- **S-piece**: S-shaped (zigzag)
- **Z-piece**: Z-shaped (zigzag)
- **J-piece**: J-shaped
- **L-piece**: L-shaped

### Basic Controls
- **Move Left/Right**: Shift piece horizontally
- **Rotate**: Turn piece 90° clockwise/counterclockwise
- **Soft Drop**: Speed up falling (hold key)
- **Hard Drop**: Instantly drop to bottom
- **Hold**: Store current piece for later use

### Game Rules

#### Line Clearing
- **Objective**: Fill complete horizontal lines without gaps
- **Clearing**: When a line is complete, it disappears
- **Cascade**: Blocks above the cleared line fall down to fill the gap

#### Scoring System
- **Single**: 1 line cleared
- **Double**: 2 lines cleared simultaneously  
- **Triple**: 3 lines cleared simultaneously
- **Tetris**: 4 lines cleared simultaneously (highest score)

#### Level Progression
- **Speed Increase**: Each level makes pieces fall faster
- **Level Up**: Typically every 10 lines cleared
- **Challenge**: Higher levels require faster decision-making

#### Game Over
- **Condition**: Stack reaches the top of the playing field
- **Result**: New pieces can't enter, game ends

## Key Features for Implementation

### Essential Features
1. **Piece Generation**: Random selection of 7 Tetrimino types
2. **Piece Movement**: Horizontal movement and rotation
3. **Collision Detection**: Prevent pieces from overlapping or going out of bounds
4. **Line Detection**: Identify complete horizontal lines
5. **Line Clearing**: Remove complete lines and drop blocks above
6. **Score Tracking**: Count points for different line clears
7. **Level System**: Increase speed based on progress

### Advanced Features
1. **Next Piece Preview**: Show upcoming piece
2. **Hold System**: Store and swap pieces
3. **Ghost Piece**: Show where current piece will land
4. **Sound Effects**: Audio feedback for actions
5. **Visual Effects**: Animations for line clearing

## Why This Structure Works for Development

This breakdown allows us to build Tetris incrementally:

1. **Start Simple**: Basic piece falling and placement
2. **Add Movement**: Horizontal movement and rotation
3. **Implement Logic**: Line detection and clearing
4. **Enhance Gameplay**: Scoring, levels, and polish
5. **Add Features**: Next piece, hold, ghost, etc.

Each milestone produces a playable version that can be tested and built upon, making the development process manageable and rewarding.
