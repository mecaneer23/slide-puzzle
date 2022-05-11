#!/usr/bin/env python3

import curses
import random

BOARD_SIZE = 3

def main(stdscr):
    curses.use_default_colors()
    board = [str(i).rjust(2, ' ') for i in ["  ", *range(1, BOARD_SIZE * BOARD_SIZE)]]
    random.shuffle(board) # this leads to an occasional issue where the board is not solvable
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
        stdscr.addstr("\nMove: ")
        key = stdscr.getkey()
        if key == 'q':
            return 'quit'
        move = key.rjust(2, ' ')
        open_space_loc = board.index('  ')
        try:
            move_loc = board.index(move)
        except ValueError:
            continue
        if open_space_loc in (
            move_loc + 1,
            move_loc - 1,
            move_loc + BOARD_SIZE,
            move_loc - BOARD_SIZE
        ):
            board[open_space_loc], board[move_loc] = board[move_loc], board[open_space_loc]
        if board == sorted(board):
            return 'win'
        stdscr.refresh()

if __name__ == "__main__":
    if curses.wrapper(main) == 'win':
        print("You Win!")
