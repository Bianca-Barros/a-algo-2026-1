"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action

    if action not in actions(board):
        raise Exception("Invalid action")

    new_board = copy.deepcopy(board)

    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Linhas
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Diagonal principal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    # Diagonal secundária
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won, -1 if O has won, 0 otherwise.
    """

    game_winner = winner(board)

    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    current_player = player(board)

    # Jogador X tenta maximizar
    if current_player == X:

        best_value = -math.inf
        best_action = None

        for action in actions(board):
            value = min_value(result(board, action))

            if value > best_value:
                best_value = value
                best_action = action

        return best_action

    # Jogador O tenta minimizar
    else:

        best_value = math.inf
        best_action = None

        for action in actions(board):
            value = max_value(result(board, action))

            if value < best_value:
                best_value = value
                best_action = action

        return best_action


def max_value(board):

    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):

    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v
