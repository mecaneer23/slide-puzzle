#!/usr/bin/env python3

from tkinter import Tk, ttk, StringVar, messagebox
import random
BOARD_SIZE = 3


def update(
    board: list[str],
    update_moves: bool,
    variables: list[list[StringVar]],
    moves: StringVar = StringVar(Tk(), "Moves: -1"),
) -> None:
    c = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            variables[i][j].set(board[c])
            c += 1
    if update_moves:
        moves.set(f"Moves: {int(moves.get().split()[-1]) + 1}")


def move(
    event=None,
    board: list = list(),
    variables: list[list[StringVar]] = [[StringVar(Tk())]],
    keycode: int | None = None,
    update_counter: bool = True,
) -> None:
    if event is not None:
        key = event.keycode
    else:
        key = keycode
    open_space_loc = board.index(" ")
    if key == 81:
        root.destroy()
        exit()
    elif key in (87, 38):
        if not (open_space_loc + BOARD_SIZE < BOARD_SIZE * BOARD_SIZE):
            return
        move_loc = open_space_loc + BOARD_SIZE
    elif key in (83, 40):
        if not (open_space_loc - BOARD_SIZE >= 0):
            return
        move_loc = open_space_loc - BOARD_SIZE
    elif key in (65, 37):
        if not (
            (open_space_loc + 1) % BOARD_SIZE != 0
            and open_space_loc + 1 < BOARD_SIZE * BOARD_SIZE
        ):
            return
        move_loc = open_space_loc + 1
    elif key in (68, 39):
        if not (open_space_loc % BOARD_SIZE != 0 and open_space_loc - 1 >= 0):
            return
        move_loc = open_space_loc - 1
    else:
        return
    board[open_space_loc], board[move_loc] = board[move_loc], board[open_space_loc]
    update(board, update_counter, variables)
    if board == sorted(board):
        if messagebox.askyesno("You win!", "Do you want to play again?"):
            root.destroy()

            init()
        else:
            root.destroy()
            exit()

def init():
    root = Tk()
    root.title("Slide Puzzle")
    board = [str(i) for i in [" ", *range(1, BOARD_SIZE * BOARD_SIZE)]]
    root.bind_all("<Key>", lambda e: move(e, board))
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
    for _ in range(10):
        move(None, board, variables, random.choice((37, 38, 39, 40)), False)
    moves.set("Moves: -1")
    ttk.Label(root, textvariable=moves).grid(
        columnspan=BOARD_SIZE, row=BOARD_SIZE + 1, column=0
    )
    update(board, True, variables)
    return root, board, moves


root, board, moves = init()
root.mainloop()