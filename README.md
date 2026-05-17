# Tic Tac Toe with Minimax Algorithm

## Overview
This project implements an AI that plays Tic Tac Toe optimally using the Minimax algorithm with alpha-beta pruning. The implementation includes game logic and a graphical user interface.

## Project Files
1. **`tictactoe.py`**: Core game logic and Minimax algorithm
2. **`runner.py`**: Graphical interface using Tkinter
3. **`tic_tac_toe_minimax.ipynb`**: Documentation and tests

## Implementation Details

### Game Logic (`tictactoe.py`)
- **`initial_state()`**: Returns empty 3x3 grid
- **`player(board)`**: Determines whose turn it is (X or O)
- **`actions(board)`**: Returns all valid moves
- **`result(board, action)`**: Returns new board after a move
- **`winner(board)`**: Checks if someone won
- **`terminal(board)`**: Checks if game is over
- **`utility(board)`**: Returns value of terminal board (+1, -1, or 0)
- **`minimax(board)`**: Determines optimal move
- **`minimax_alpha_beta(board)`**: Optimized Minimax algorithm

### GUI (`runner.py`)
- 3x3 grid of buttons for the game board
- Handles player moves and AI responses
- Displays game status
- Includes reset button

## How to Run
run `runner.py`, it will open a window to play

## How to Play
1. Click on an empty cell to place X
2. AI responds with O
3. Try to get three in a row
4. Click "New Game" to restart

## Features
- Unbeatable AI using Minimax algorithm
- Alpha-beta pruning for optimization
- Simple user interface
