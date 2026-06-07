def check_winner(board, player):

    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Main diagonal
    if all(board[i][i] == player for i in range(3)):
        return True

    # Other diagonal
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):

    for row in board:
        if "" in row:
            return False

    return True


def get_available_moves(board):

    moves = []

    for row in range(3):
        for col in range(3):

            if board[row][col] == "":
                moves.append((row, col))

    return moves