# Tetris Development Plan

## Project Milestones

### Milestone 1: Basic Game Foundation
**Goal**: Create a playable prototype with falling pieces
**Deliverable**: Simple Tetris where pieces fall and stack

#### Tasks:
- [x] Set up project structure and dependencies
- [x] Create game window and basic rendering
- [ ] Implement 7 Tetrimino shapes
- [ ] Add piece falling mechanics
- [ ] Basic collision detection (bottom and sides)
- [ ] Piece placement and stacking
- [ ] **Debug Mode**: Full control system for testing
  - [ ] Skip any upcoming piece
  - [ ] Generate and place any piece in legal positions
  - [ ] Clear any existing piece or line
  - [ ] Toggle between debug and normal play

**Test Criteria**: ✅ Game window displays correctly (800x600, 60 FPS, black background), ⏳ Pieces fall, stack at bottom, debug mode works for all features

---

### Milestone 2: Core Gameplay
**Goal**: Add movement controls and line clearing
**Deliverable**: Fully functional basic Tetris

#### Tasks:
- [ ] Implement piece rotation (4 directions)
- [ ] Add horizontal movement controls
- [ ] Implement soft drop and hard drop
- [ ] Create line detection algorithm
- [ ] Add line clearing mechanics
- [ ] Implement block falling after line clear

**Test Criteria**: Can move and rotate pieces, clear lines, blocks fall properly

---

### Milestone 3: Game Systems
**Goal**: Add scoring, levels, and game over logic
**Deliverable**: Complete Tetris game with progression

#### Tasks:
- [ ] Implement scoring system (single, double, triple, tetris)
- [ ] Add level progression (every 10 lines)
- [ ] Implement speed increase per level
- [ ] Add game over detection
- [ ] Create restart functionality
- [ ] Add basic UI (score, level, lines display)

**Test Criteria**: Score increases correctly, speed increases with levels, game ends when stack reaches top

---

### Milestone 4: Enhanced Features
**Goal**: Add quality-of-life improvements
**Deliverable**: Polished Tetris with modern features

#### Tasks:
- [ ] Add next piece preview
- [ ] Implement hold system
- [ ] Add ghost piece indicator
- [ ] Create pause functionality
- [ ] Add basic sound effects
- [ ] Improve visual feedback

**Test Criteria**: All features work correctly, game feels polished

---

### Milestone 5: Polish and Optimization
**Goal**: Final polish and performance optimization
**Deliverable**: Production-ready Tetris game

#### Tasks:
- [ ] Add visual effects for line clearing
- [ ] Implement particle effects
- [ ] Add background music
- [ ] Create settings menu
- [ ] Add high score system
- [ ] **Control Customization**: Change and view current controls
  - [ ] Settings interface for key remapping
  - [ ] Display current control scheme
  - [ ] Save/load control preferences
- [ ] **Screen Responsiveness**: Multiple resolution support
  - [ ] Resolution options (800x600, 1024x768, 1920x1080, etc.)
  - [ ] Responsive UI scaling
  - [ ] Fullscreen mode support
- [ ] Performance optimization
- [ ] Code cleanup and documentation

**Test Criteria**: Game runs smoothly, all features work, code is well-documented, controls customizable, responsive on different resolutions

---

### Milestone 6: Multiplayer Support
**Goal**: Add local multiplayer functionality
**Deliverable**: 2-player simultaneous Tetris

#### Tasks:
- [ ] **Multiplayer Architecture**: Support for 2 players
  - [ ] Split-screen game window (vertical or horizontal division)
  - [ ] Separate game states for each player
  - [ ] Independent scoring and level progression
- [ ] **Player Controls**: Different keybindings per player
  - [ ] Player 1: WASD + Space + Shift
  - [ ] Player 2: Arrow keys + Enter + Right Shift
  - [ ] Customizable per-player controls
- [ ] **Multiplayer UI**: Enhanced interface
  - [ ] Side-by-side or top-bottom game views
  - [ ] Separate score displays
  - [ ] Game over handling for both players
- [ ] **Multiplayer Features**:
  - [ ] Simultaneous gameplay
  - [ ] Independent piece generation
  - [ ] Separate hold systems
  - [ ] Winner determination logic

**Test Criteria**: Both players can play simultaneously, different controls work independently, game handles both players' game over states

## Development Phases
1. **Foundation** (M1-2): Core mechanics, game loop, line clearing
2. **Systems** (M3): Scoring, levels, game over
3. **Enhancement** (M4-5): Modern features, polish, customization
4. **Multiplayer** (M6): 2-player split-screen

## Architecture
**Core**: Game engine, board system, piece system, input handler, renderer  
**Structure**: Modular `src/` with game/, config/, tests/ folders  
**Security**: No hardcoded secrets, proper .env handling

## Testing
**Unit**: Piece logic, collision, scoring  
**Integration**: Game cycles, progression  
**Manual**: Gameplay feel, edge cases

## Success Criteria
**M1**: Pieces fall/stack, 60 FPS, no visual glitches  
**M2**: Responsive controls, perfect line clearing  
**M3**: Accurate scoring, proper level progression  
**M4**: Enhanced gameplay, good performance  
**M5**: Production quality, optimized, customizable  
**M6**: Working 2-player split-screen

## Risk Management
**Technical**: Focus milestones, regular testing, avoid complexity creep  
**Scope**: Core mechanics first, playable milestones, maintain quality

---

**Last Updated**: September 19, 2025
**Current Milestone**: Milestone 1 - Basic Game Foundation (2/8 tasks complete)
**Total Milestones**: 6 (including multiplayer support)
**Next Review**: After Milestone 1 completion

## Progress Log

**Sep 19, 2025**: ✅ M1 Tasks 1-2 complete - Project structure + game window (8/8 tests passing)  
**Next**: Task 3 - Implement 7 Tetrimino shapes
