"""Tic Tac Toe Game Logic"""

def initial_state():
    """Returns starting state of the board - a 3x3 grid of None values."""
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]


def player(board):
    """Returns player who has the next turn on a board."""
    # Count number of X's and O's
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    # X goes first, so if there are equal numbers of X and O, then it's X's turn
    return "X" if x_count <= o_count else "O"


def actions(board):
    """Returns set of all possible actions (i, j) available on the board."""
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """Returns board that would result from action."""
    # Create a deep copy of the board
    new_board = [row[:] for row in board]

    i, j = action

    # Check if the action is valid
    if new_board[i][j] is not None:
        raise Exception("Invalid action!")

    # Make the move
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """Returns the winner of the board, if there is one."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """Returns True if game is over, False otherwise."""
    # Check if there's a winner
    if winner(board) is not None:
        return True

    # Check if there are no more possible actions
    for row in board:
        if None in row:
            return False

    return True


def utility(board):
    """Returns 1 if X has won the game, -1 if O has won, 0 otherwise."""
    game_winner = winner(board)

    if game_winner == "X":
        return 1
    elif game_winner == "O":
        return -1
    else:
        return 0


def minimax(board):
    """Returns the optimal action for the current player on the board."""
    # Use more efficient alpha-beta pruning version
    return minimax_alpha_beta(board)


def minimax_alpha_beta(board):
    """Returns the optimal action using alpha-beta pruning."""
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == "X":
        # X wants to maximize
        best_val = float('-inf')
        best_action = None

        for action in actions(board):
            val = min_value(result(board, action), float('-inf'), float('inf'))
            if val > best_val:
                best_val = val
                best_action = action

        return best_action
    else:
        # O wants to minimize
        best_val = float('inf')
        best_action = None

        for action in actions(board):
            val = max_value(result(board, action), float('-inf'), float('inf'))
            if val < best_val:
                best_val = val
                best_action = action

        return best_action


def max_value(board, alpha, beta):
    """Returns the maximum utility possible from the board."""
    if terminal(board):
        return utility(board)

    v = float('-inf')

    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)

    return v


def min_value(board, alpha, beta):
    """Returns the minimum utility possible from the board."""
    if terminal(board):
        return utility(board)

    v = float('inf')

    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)

    return v
