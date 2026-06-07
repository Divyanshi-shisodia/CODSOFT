import tkinter as tk
from minimax import best_move
from game_logic import check_winner, is_draw

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

buttons = []

root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.geometry("400x500")

status_label = tk.Label(root, text="Your Turn (X)", font=("Arial", 14))
status_label.pack(pady=10)


def ai_turn():
    move = best_move(board)

    if move:
        row, col = move
        board[row][col] = "O"
        buttons[row][col].config(text="O")

    if check_winner(board, "O"):
        status_label.config(text="AI Wins!")
        disable_buttons()
        return

    if is_draw(board):
        status_label.config(text="Draw!")
        return

    status_label.config(text="Your Turn (X)")


def player_move(row, col):

    if board[row][col] != "":
        return

    board[row][col] = "X"
    buttons[row][col].config(text="X")

    if check_winner(board, "X"):
        status_label.config(text="You Win!")
        disable_buttons()
        return

    if is_draw(board):
        status_label.config(text="Draw!")
        return

    status_label.config(text="AI Thinking...")
    root.after(500, ai_turn)


def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state="disabled")


def restart_game():

    global board

    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    for row in buttons:
        for button in row:
            button.config(text="", state="normal")

    status_label.config(text="Your Turn (X)")


frame = tk.Frame(root)
frame.pack()

for row in range(3):

    button_row = []

    for col in range(3):

        button = tk.Button(
            frame,
            text="",
            font=("Arial", 24),
            width=5,
            height=2,
            command=lambda r=row, c=col: player_move(r, c)
        )

        button.grid(row=row, column=col)

        button_row.append(button)

    buttons.append(button_row)

restart_btn = tk.Button(
    root,
    text="Restart",
    font=("Arial", 12),
    command=restart_game
)

restart_btn.pack(pady=20)

root.mainloop()