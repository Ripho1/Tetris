# Tetris Game

![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/Ripho1/Tetris?utm_source=oss&utm_medium=github&utm_campaign=Ripho1%2FTetris&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)

A classic Tetris implementation built with Python and Pygame, featuring modern game development practices and comprehensive testing.

## 🎮 About

This project implements the classic Tetris puzzle game with falling geometric shapes (Tetriminos) that players must arrange to create complete horizontal lines. The game includes all traditional Tetris mechanics with plans for modern enhancements.

## ✨ Features

### Planned Features
- 🎯 **Core Gameplay**: Piece movement, rotation, and line clearing
- 🎯 **Game Systems**: Scoring, levels, and game over logic
- 🎯 **Enhanced Features**: Next piece preview, hold system, ghost piece
- 🎯 **Multiplayer**: 2-player split-screen support
- 🎯 **Customization**: Control remapping and resolution options

## 🚀 Quick Start

### Prerequisites
- Python 3.9, 3.10, 3.11, 3.12, or 3.13
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ripho1/Tetris.git
   cd Tetris
   ```

2. **Activate the virtual environment**
   
   **Windows (Git Bash/PowerShell):**
   ```bash
   source .venv/Scripts/activate
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   .venv\Scripts\activate.bat
   ```
   
   **Linux/Mac:**
   ```bash
   source .venv/bin/activate
   ```
   
   > **Note**: If you don't have the virtual environment set up yet, install dependencies first:
   > ```bash
   > pip install -r requirements.txt
   > ```

3. **Run the game**
   ```bash
   python main.py
   ```
   
   **Or use the convenient commands:**
   ```bash
   python commands.py game    # Run the Tetris game
   python commands.py test    # Run all tests
   python commands.py help    # Show all available commands
   ```

## 🎯 Controls

### Basic Controls
- **Move Left/Right**: Arrow keys or A/D
- **Rotate**: Up arrow or W
- **Soft Drop**: Down arrow or S
- **Hard Drop**: Space bar
- **Pause**: P (shows a semi-transparent "Paused" overlay with restart/quit)
- **Restart**: R
- **Quit**: ESC

### Debug Controls
- **Toggle Debug Mode**: F1 (enables all debug actions and shows info overlay)
- **Step Fall**: F2 (advance one fall step, works while paused)
- **Cycle Active Piece**: F3 (switches to next piece type at spawn if valid)
- **Select Row**: Up/Down while paused (choose a row to clear)
- **Clear Selected Row**: L or Delete
- **Clear Placed Piece**: Left-click a filled cell

## 🏗️ Project Structure

See [Project Structure](readme/project_structure.md) for detailed information about the codebase organization.

## 🧪 Testing

The project includes comprehensive testing with pytest:

```bash
# Activate virtual environment first
source .venv/Scripts/activate  # Windows Git Bash/PowerShell
# .venv\Scripts\activate.bat   # Windows Command Prompt
# source .venv/bin/activate     # Linux/Mac

# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_piece.py

# Or use the convenient command
python commands.py test
```

## 📋 Development Status

See [Development Plan](readme/development_plan.md) for detailed milestone information.

## 🛠️ Development

### Code Quality
This project follows strict development standards:
- **Python Best Practices**: Type hints, docstrings, and clean code
- **Testing**: Comprehensive unit and integration tests
- **Documentation**: Detailed README files and inline documentation
- **Code Review**: Automated checks and CodeRabbit integration

### Contributing
1. Fork the repository
2. Create a feature branch
3. Follow the coding standards in `cursor-rules/`
4. Add tests for new features
5. Submit a pull request

## 📚 Documentation

- [Game Overview](readme/game_overview.md) - Detailed game mechanics and rules
- [Development Plan](readme/development_plan.md) - Complete development roadmap
- [Project Structure](readme/project_structure.md) - Additional documentation files
- [Configuration Guide](readme/configuration_guide.md) - How to customize game settings

## 🎮 Game Rules

### Basic Mechanics
- **Playing Field**: 10 columns × 20 rows
- **Objective**: Fill complete horizontal lines to clear them
- **Scoring**: Points for single, double, triple, and Tetris (4-line) clears
- **Progression**: Speed increases with each level (every 10 lines)

### Tetrimino Shapes
- **I-piece**: Straight line (4 squares)
- **O-piece**: 2×2 square
- **T-piece**: T-shaped
- **S-piece**: S-shaped zigzag
- **Z-piece**: Z-shaped zigzag
- **J-piece**: J-shaped
- **L-piece**: L-shaped

## 🐛 Bug Reports

Found a bug? Please create an issue with:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior
- System information (OS, Python version)

## 📄 License

This project is open source. See the repository for license details.

## 🙏 Acknowledgments

- Classic Tetris game mechanics
- Pygame community for excellent documentation
- Python community for best practices and tools

---

**Built with ❤️ using Python and Pygame**
