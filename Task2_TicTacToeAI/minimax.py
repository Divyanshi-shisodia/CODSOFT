from game_logic import check_winner, is_draw, get_available_moves

AI = "O"
HUMAN = "X"


def minimax(board, depth, is_maximizing):

    if check_winner(board, AI):
        return 1

    if check_winner(board, HUMAN):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:

        best_score = -1000

        for row, col in get_available_moves(board):

            board[row][col] = AI

            score = minimax(board, depth + 1, False)

            board[row][col] = ""

            best_score = max(score, best_score)

        return best_score

    else:

        best_score = 1000

        for row, col in get_available_moves(board):

            board[row][col] = HUMAN

            score = minimax(board, depth + 1, True)

            board[row][col] = ""

            best_score = min(score, best_score)

        return best_score


def best_move(board):

    best_score = -1000
    move = None

    for row, col in get_available_moves(board):

        board[row][col] = AI

        score = minimax(board, 0, False)

        board[row][col] = ""

        if score > best_score:
            best_score = score
            move = (row, col)

    return move