from game_logic import check_winner, is_draw, get_available_moves

AI = "O"
HUMAN = "X"


def minimax(board, depth, is_maximizing, alpha, beta):

    if check_winner(board, AI):
        return 10 - depth

    if check_winner(board, HUMAN):
        return depth - 10

    if is_draw(board):
        return 0

    if is_maximizing:

        best_score = -1000

        for row, col in get_available_moves(board):

            board[row][col] = AI

            score = minimax(
                board,
                depth + 1,
                False,
                alpha,
                beta
            )

            board[row][col] = ""

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best_score

    else:

        best_score = 1000

        for row, col in get_available_moves(board):

            board[row][col] = HUMAN

            score = minimax(
                board,
                depth + 1,
                True,
                alpha,
                beta
            )

            board[row][col] = ""

            best_score = min(best_score, score)

            beta = min(beta, best_score)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best_score


def best_move(board):

    best_score = -1000
    move = None

    for row, col in get_available_moves(board):

        board[row][col] = AI

        score = minimax(
            board,
            0,
            False,
            -1000,
            1000
        )

        board[row][col] = ""

        if score > best_score:

            best_score = score
            move = (row, col)

    return move