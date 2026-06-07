import tkinter as tk
import random

from minimax import best_move
from game_logic import check_winner, is_draw

# ------------------------
# GAME DATA
# ------------------------

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

buttons = []

wins = 0
losses = 0
draws = 0
moves_played = 0

# ------------------------
# WINDOW
# ------------------------

root = tk.Tk()
root.title("🤖 Tic-Tac-Toe AI Agent")
root.geometry("500x700")
root.configure(bg="#1e1e1e")

# ------------------------
# TITLE
# ------------------------

title_label = tk.Label(
    root,
    text="🤖 Tic-Tac-Toe AI",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)

title_label.pack(pady=10)

# ------------------------
# SCOREBOARD
# ------------------------

score_label = tk.Label(
    root,
    text="Wins: 0 | Losses: 0 | Draws: 0",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

score_label.pack(pady=5)

# ------------------------
# MOVE COUNTER
# ------------------------

moves_label = tk.Label(
    root,
    text="Moves: 0",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

moves_label.pack()

# ------------------------
# DIFFICULTY
# ------------------------

difficulty = tk.StringVar()
difficulty.set("Hard")

difficulty_label = tk.Label(
    root,
    text="Difficulty",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12)
)

difficulty_label.pack()

difficulty_menu = tk.OptionMenu(
    root,
    difficulty,
    "Easy",
    "Medium",
    "Hard"
)

difficulty_menu.pack(pady=5)

# ------------------------
# STATUS
# ------------------------

status_label = tk.Label(
    root,
    text="Your Turn (X)",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="white"
)

status_label.pack(pady=10)

# ------------------------
# FUNCTIONS
# ------------------------

def update_score():
    score_label.config(
        text=f"Wins: {wins} | Losses: {losses} | Draws: {draws}"
    )


def update_moves():
    moves_label.config(
        text=f"Moves: {moves_played}"
    )


def random_move():

    available = []

    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                available.append((r, c))

    if available:
        return random.choice(available)

    return None


def highlight_winner(player):

    # Rows
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            for col in range(3):
                buttons[row][col].config(bg="green")
            return

    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            for row in range(3):
                buttons[row][col].config(bg="green")
            return

    # Main diagonal
    if all(board[i][i] == player for i in range(3)):
        for i in range(3):
            buttons[i][i].config(bg="green")
        return

    # Other diagonal
    if all(board[i][2-i] == player for i in range(3)):
        for i in range(3):
            buttons[i][2-i].config(bg="green")
        return


def disable_buttons():

    for row in buttons:
        for button in row:
            button.config(state="disabled")


def ai_turn():

    global losses, draws, moves_played

    level = difficulty.get()

    if level == "Easy":

        move = random_move()

    elif level == "Medium":

        if random.random() < 0.5:
            move = random_move()
        else:
            move = best_move(board)

    else:

        move = best_move(board)

    if move:

        row, col = move

        board[row][col] = "O"

        buttons[row][col].config(text="O")

        moves_played += 1
        update_moves()

    if check_winner(board, "O"):

        losses += 1
        update_score()

        highlight_winner("O")

        status_label.config(text="🤖 AI Wins!")

        disable_buttons()

        return

    if is_draw(board):

        draws += 1
        update_score()

        status_label.config(text="🤝 Draw!")

        return

    status_label.config(text="Your Turn (X)")


def player_move(row, col):

    global wins, draws, moves_played

    if board[row][col] != "":
        return

    board[row][col] = "X"

    buttons[row][col].config(text="X")

    moves_played += 1
    update_moves()

    if check_winner(board, "X"):

        wins += 1
        update_score()

        highlight_winner("X")

        status_label.config(text="🎉 You Win!")

        disable_buttons()

        return

    if is_draw(board):

        draws += 1
        update_score()

        status_label.config(text="🤝 Draw!")

        return

    status_label.config(text="🤖 AI Thinking...")

    root.after(800, ai_turn)


def restart_game():

    global board, moves_played

    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    moves_played = 0
    update_moves()

    for row in buttons:
        for button in row:

            button.config(
                text="",
                state="normal",
                bg="#2d2d2d"
            )

    status_label.config(text="Your Turn (X)")


def show_about():

    about_window = tk.Toplevel(root)

    about_window.title("About")

    tk.Label(
        about_window,
        text="""
Tic-Tac-Toe AI

Features:
• Minimax Algorithm
• Alpha-Beta Pruning
• Difficulty Levels
• Score Tracking
• Move Counter

Developed by Divyanshi
        """,
        font=("Arial", 12)
    ).pack(padx=20, pady=20)

# ------------------------
# BOARD
# ------------------------

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=20)

for row in range(3):

    button_row = []

    for col in range(3):

        button = tk.Button(
            frame,
            text="",
            font=("Arial", 24, "bold"),
            width=5,
            height=2,
            bg="#2d2d2d",
            fg="white",
            activebackground="#444444",
            command=lambda r=row, c=col: player_move(r, c)
        )

        button.grid(
            row=row,
            column=col,
            padx=5,
            pady=5
        )

        button_row.append(button)

    buttons.append(button_row)

# ------------------------
# BUTTONS
# ------------------------

restart_button = tk.Button(
    root,
    text="🔄 Restart Game",
    font=("Arial", 12, "bold"),
    bg="#444444",
    fg="white",
    command=restart_game
)

restart_button.pack(pady=10)

about_button = tk.Button(
    root,
    text="ℹ About",
    font=("Arial", 12),
    bg="#444444",
    fg="white",
    command=show_about
)

about_button.pack(pady=5)

# ------------------------
# FOOTER
# ------------------------

footer = tk.Label(
    root,
    text="Developed by Divyanshi",
    bg="#1e1e1e",
    fg="gray"
)

footer.pack(side="bottom", pady=10)

# ------------------------
# RUN
# ------------------------

root.mainloop()