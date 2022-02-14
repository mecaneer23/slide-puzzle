#!/usr/bin/env python3

import curses
import random

BOARD_SIZE = 3

def main(stdscr):
    board = ['  ']
    board.extend(range(1, BOARD_SIZE * BOARD_SIZE))
    board = [str(i).rjust(2, ' ') for i in board]
    random.shuffle(board) # this leads to an occasional issue where the board is not solvable
    moves = 0
    stdscr.nodelay(0)
    while True:
        stdscr.clear()
        stdscr.addstr(f"Moves: {moves}\n\n")
        moves += 1
        stdscr.addstr("    ")
        counter = 1
        for piece in board:
            stdscr.addstr(f"{piece} ")
            if counter % BOARD_SIZE == 0:
                stdscr.addstr("\n    ")
            counter += 1
        stdscr.addstr("\n")
        # move = input("Move: ").rjust(2, ' ')
        stdscr.addstr("Move: ")
        key = stdscr.getkey()
        if key == 'q':
            return 'q'
        move = key.rjust(2, ' ')
        open_space_loc = board.index('  ')
        try:
            move_loc = board.index(move)
        except ValueError:
            continue
        if (
            move_loc + 1 == open_space_loc
            or move_loc - 1 == open_space_loc
            or move_loc + BOARD_SIZE == open_space_loc
            or move_loc - BOARD_SIZE == open_space_loc
        ):
            board[open_space_loc], board[move_loc] = board[move_loc], board[open_space_loc]
        if board == sorted(board):
            return 'w'
        stdscr.addstr("-" * 20)
        stdscr.refresh()

if __name__ == "__main__":
    if curses.wrapper(main) == 'w':
        print("You Win!")
