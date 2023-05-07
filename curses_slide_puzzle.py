#!/usr/bin/env python3

import curses
import random

BOARD_SIZE = 3


def main(stdscr):
    curses.use_default_colors()
    curses.curs_set(0)
    board = [str(i).rjust(2, " ") for i in ["  ", *range(1, BOARD_SIZE * BOARD_SIZE)]]
    random.shuffle(
        board
    )  # this leads to an occasional issue where the board is not solvable
    moves = 0
    stdscr.nodelay(0)
    while True:
        stdscr.clear()
        stdscr.addstr(f"Moves: {moves}\n\n    ")
        moves += 1
        for i, piece in enumerate(board, 1):
            stdscr.addstr(f"{piece} ")
            if i % BOARD_SIZE == 0:
                stdscr.addstr("\n    ")
        key = stdscr.getkey()
        open_space_loc = board.index("  ")
        if key == "q":
            return ""
        elif key in ("KEY_UP", "w"):
            if open_space_loc + BOARD_SIZE < BOARD_SIZE * BOARD_SIZE:
                move_loc = open_space_loc + BOARD_SIZE
            else:
                continue
        elif key in ("KEY_DOWN", "s"):
            if open_space_loc - BOARD_SIZE >= 0:
                move_loc = open_space_loc - BOARD_SIZE
            else:
                continue
        elif key in ("KEY_LEFT", "a"):
            if (
                open_space_loc + 1
            ) % BOARD_SIZE != 0 and open_space_loc + 1 < BOARD_SIZE * BOARD_SIZE:
                move_loc = open_space_loc + 1
            else:
                continue
        elif key in ("KEY_RIGHT", "d"):
            if open_space_loc % BOARD_SIZE != 0 and open_space_loc - 1 >= 0:
                move_loc = open_space_loc - 1
            else:
                continue
        else:
            continue
        if key:
            board[open_space_loc], board[move_loc] = (
                board[move_loc],
                board[open_space_loc],
            )
        if board == sorted(board):
            return "You win!\n"
        stdscr.refresh()


if __name__ == "__main__":
    print(curses.wrapper(main), end="")
