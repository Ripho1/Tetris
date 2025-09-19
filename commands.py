#!/usr/bin/env python3
"""
Commands Script for Tetris Game

This script provides convenient commands to run the game and tests.
Usage:
    python commands.py game    - Run the Tetris game
    python commands.py test    - Run all tests
    python commands.py help    - Show this help message
"""

import sys
import subprocess
import os


def run_game():
    """
    Run the Tetris game.

    Executes the main.py file to start the game.
    """
    print("Starting Tetris game...")
    try:
        subprocess.run([sys.executable, "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running game: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nGame interrupted by user")


def run_tests():
    """
    Run all tests using pytest.

    Executes pytest with verbose output to show test results clearly.
    """
    print("Running tests...")
    try:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "tests/",
                "-v",
                "--tb=short",  # Short traceback format
            ],
            check=True,
        )
        print("All tests passed!")
    except subprocess.CalledProcessError as e:
        print(f"Some tests failed. Exit code: {e.returncode}")
        sys.exit(1)


def show_help():
    """
    Display help information about available commands.
    """
    print(__doc__)
    print("\nAvailable commands:")
    print("  game    - Run the Tetris game")
    print("  test    - Run all tests")
    print("  help    - Show this help message")
    print("\nExamples:")
    print("  python commands.py game")
    print("  python commands.py test")


def main():
    """
    Main function that parses command line arguments and executes commands.
    """
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one command.")
        show_help()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "game":
        run_game()
    elif command == "test":
        run_tests()
    elif command == "help":
        show_help()
    else:
        print(f"Error: Unknown command '{command}'")
        show_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
