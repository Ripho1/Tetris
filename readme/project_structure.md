# Project Structure

## Overview
This Tetris project follows a modular architecture with clear separation of concerns, making it easy to maintain and extend.

## Directory Structure

```
Tetris/
├── src/                    # Source code
│   ├── game/              # Core game logic
│   │   ├── engine.py      # Main game engine and loop
│   │   ├── board.py       # Game board management
│   │   ├── piece.py       # Tetrimino piece logic
│   │   └── piece_factory.py # Piece generation and creation
│   └── config/            # Configuration
│       └── settings.py    # Game settings and constants
├── tests/                 # Test suite
│   ├── test_basic_setup.py # Basic project setup tests
│   ├── test_board.py      # Board functionality tests
│   ├── test_piece.py      # Piece logic tests
│   ├── test_piece_factory.py # Piece factory tests
│   └── test_commands.py   # Command system tests
├── readme/               # Detailed documentation
│   ├── game_overview.md  # Game mechanics and rules
│   ├── development_plan.md # Development roadmap
│   └── project_structure.md # This file
├── cursor-rules/         # Development guidelines
│   ├── expert-python.yaml # Python best practices
│   ├── game-structure.yaml # Game development patterns
│   ├── beginner-friendly.yaml # Code readability guidelines
│   ├── testing.yaml      # Testing standards
│   └── documentation.yaml # Documentation requirements
├── .github/workflows/    # CI/CD configuration
│   └── pr-checks.yml     # GitHub Actions workflow
├── main.py              # Application entry point
├── commands.py          # Development command utilities
└── requirements.txt     # Python dependencies
```

## Key Components

### Core Game Logic (`src/game/`)
- **engine.py**: Main game loop, event handling, and game state management
- **board.py**: Game board representation, line clearing, and collision detection
- **piece.py**: Individual Tetrimino piece behavior and rotation logic
- **piece_factory.py**: Piece creation, random generation, and shape definitions

### Configuration (`src/config/`)
- **settings.py**: Game constants, window dimensions, colors, and timing settings

### Testing (`tests/`)
- Comprehensive test coverage for all major components
- Unit tests for individual functions and classes
- Integration tests for component interactions

### Documentation (`readme/`)
- **game_overview.md**: Detailed game mechanics and rules
- **development_plan.md**: Complete development roadmap with milestones
- **project_structure.md**: This file - codebase organization

### Development Standards (`cursor-rules/`)
- YAML configuration files defining coding standards
- Python best practices and game development patterns
- Testing and documentation requirements

## Architecture Principles

1. **Modularity**: Each component has a single responsibility
2. **Testability**: All components are designed for easy testing
3. **Extensibility**: Clear interfaces allow for easy feature additions
4. **Documentation**: Comprehensive documentation for all components
5. **Standards**: Consistent coding practices across the project

## File Naming Conventions

- **Python files**: snake_case (e.g., `piece_factory.py`)
- **Test files**: `test_` prefix (e.g., `test_piece.py`)
- **Documentation**: kebab-case (e.g., `project-structure.md`)
- **Configuration**: descriptive names (e.g., `pr-checks.yml`)

## Dependencies

- **pygame**: Game development framework
- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Code linting

This structure supports the project's goal of creating a maintainable, well-tested Tetris implementation that can grow from a basic prototype to a full-featured game.
