#!/usr/bin/env python3

from tkinter import Tk, ttk, StringVar, messagebox
import random

BOARD_SIZE = 3  # any int, > 2
root = None
board = None
moves = None


def update(board, variables, moves=None):
    c = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            variables[i][j].set(board[c])
            c += 1
    if moves is not None:
        moves.set(f"Moves: {int(moves.get().split()[-1]) + 1}")


def move(event, board, moves, variables):
    if isinstance(event, int):
        key = event
    else:
        key = event.keycode
    open_space_loc = board.index(" ")
    if key == 81:  # q
        root.destroy()
        exit()
    elif key in (87, 38):  # w, up
        if not (open_space_loc + BOARD_SIZE < BOARD_SIZE * BOARD_SIZE):
            return
        move_loc = open_space_loc + BOARD_SIZE
    elif key in (83, 40):  # s, down
        if not (open_space_loc - BOARD_SIZE >= 0):
            return
        move_loc = open_space_loc - BOARD_SIZE
    elif key in (65, 37):  # a, left
        if not (
            (open_space_loc + 1) % BOARD_SIZE != 0
            and open_space_loc + 1 < BOARD_SIZE * BOARD_SIZE
        ):
            return
        move_loc = open_space_loc + 1
    elif key in (68, 39):  # d, right
        if not (open_space_loc % BOARD_SIZE != 0 and open_space_loc - 1 >= 0):
            return
        move_loc = open_space_loc - 1
    else:
        return
    board[open_space_loc], board[move_loc] = board[move_loc], board[open_space_loc]
    update(board, variables, moves)
    if board == sorted(board) and moves:
        if messagebox.askyesno("You win!", "Do you want to play again?"):
            root.destroy()
            main()
        else:
            exit()


def init():
    root = Tk()
    root.title("Slide Puzzle")
    board = [str(i) for i in [" ", *range(1, BOARD_SIZE * BOARD_SIZE)]]
    style = ttk.Style()
    style.configure(
        "Box.TLabel",
        font=("Helvetica", 64),
        width=3,
        height=3,
        borderwidth=1,
        relief="ridge",
    )
    style.configure(
        "TLabel",
    )
    count = iter(board)
    variables = [
        [StringVar(root, next(count)) for _ in range(BOARD_SIZE)]
        for _ in range(BOARD_SIZE)
    ]
    [
        [
            ttk.Label(
                root, textvariable=variables[i][j], padding=5, style=f"Box.TLabel"
            ).grid(row=i, column=j)
            for j in range(BOARD_SIZE)
        ]
        for i in range(BOARD_SIZE)
    ]
    moves = StringVar(root)
    moves.set("Moves: -1")
    root.bind_all("<Key>", lambda e: move(e, board, moves, variables))
    for _ in range(1000):
        move(random.choice((37, 38, 39, 40)), board, None, variables)
    moves.set("Moves: -1")
    ttk.Label(root, textvariable=moves).grid(
        columnspan=BOARD_SIZE, row=BOARD_SIZE + 1, column=0
    )
    update(board, variables, moves)
    return root, board, moves


def main():
    global root, board, moves
    root, board, moves = init()
    root.mainloop()


if __name__ == "__main__":
    main()
