#!/usr/bin/env python3

from tkinter import Tk, ttk, StringVar, messagebox
import random

BOARD_SIZE = 4


def main():
    def update_vars(board):
        c = 0
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                vars[i][j].set(board[c])
                c += 1
        moves.set(f"Moves: {int(moves.get().split()[-1]) + 1}")
        # print(
        #     [[vars[j][i].get() for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
        # )

    def move(event=None, keycode=None):
        nonlocal vars
        if event is not None:
            key = event.keycode
        else:
            key = keycode
        open_space_loc = board.index(" ")
        if key == 81:
            root.destroy()
            exit()
        elif key in (87, 38):
            if open_space_loc + BOARD_SIZE < BOARD_SIZE * BOARD_SIZE:
                move_loc = open_space_loc + BOARD_SIZE
            else:
                return
        elif key in (83, 40):
            if open_space_loc - BOARD_SIZE >= 0:
                move_loc = open_space_loc - BOARD_SIZE
            else:
                return
        elif key in (65, 37):
            if (
                open_space_loc + 1
            ) % BOARD_SIZE != 0 and open_space_loc + 1 < BOARD_SIZE * BOARD_SIZE:
                move_loc = open_space_loc + 1
            else:
                return
        elif key in (68, 39):
            if open_space_loc % BOARD_SIZE != 0 and open_space_loc - 1 >= 0:
                move_loc = open_space_loc - 1
            else:
                return
        else:
            return
        board[open_space_loc], board[move_loc] = board[move_loc], board[open_space_loc]
        update_vars(board)
        if board == sorted(board):
            if messagebox.askyesno("You win!", "Do you want to play again?"):
                main()

    root = Tk()
    root.title("Slide Puzzle")
    root.bind_all("<Key>", move)
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
    vars = [
        [StringVar(root, next(count)) for _ in range(BOARD_SIZE)]
        for _ in range(BOARD_SIZE)
    ]
    [
        [
            ttk.Label(
                root, textvariable=vars[i][j], padding=5, style=f"Box.TLabel"
            ).grid(row=i, column=j)
            for j in range(BOARD_SIZE)
        ]
        for i in range(BOARD_SIZE)
    ]
    for _ in range(1000):
        move(None, random.choice((37, 38, 39, 40)))
        moves = StringVar(root, "Moves: -1")
    ttk.Label(root, textvariable=moves).grid(columnspan=BOARD_SIZE, row=BOARD_SIZE + 1, column=0)
    update_vars(board)
    root.mainloop()


main()
