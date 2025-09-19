"""
Commands Script Tests

Tests to verify the commands script functionality.
"""

import subprocess
import sys


def test_commands_help():
    """Test that the help command works correctly."""
    result = subprocess.run(
        [sys.executable, "commands.py", "help"], capture_output=True, text=True
    )

    assert result.returncode == 0
    assert "Commands Script for Tetris Game" in result.stdout
    assert "game" in result.stdout
    assert "test" in result.stdout


def test_commands_invalid():
    """Test that invalid commands show error and help."""
    result = subprocess.run(
        [sys.executable, "commands.py", "invalid"], capture_output=True, text=True
    )

    assert result.returncode == 1
    assert "Unknown command 'invalid'" in result.stdout
    assert "Available commands:" in result.stdout


def test_commands_no_args():
    """Test that no arguments shows error and help."""
    result = subprocess.run(
        [sys.executable, "commands.py"], capture_output=True, text=True
    )

    assert result.returncode == 1
    assert "Please provide exactly one command" in result.stdout
