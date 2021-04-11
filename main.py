#!/usr/bin/env python
import numpy as np
import sys
from collections import deque


# BOARD
class Board:
    def __init__(self):
        self.board = np.zeros((3, 3))

    # Insert
    def insert(self, coords, player):
        x = coords[0] - 1
        y = coords[1] - 1
        self.board[x, y] = player

    # Display
    def display(self):
        for item in self.board:
            for second_item in item:
                if second_item == 0:
                    yield "[ ]"
                if second_item == 1:
                    yield "[X]"
                if second_item == 2:
                    yield "[O]"

    # Reset
    def reset(self):
        """Reset the self.board to zero"""
        self.board = np.zeros((3, 3))

    def check_win(self):
        """Check if there is a player that won"""
        # The top left to the bottom right
        diagonal_one = np.trace(self.board) / 3
        diagonal_two = np.trace(self.board[::-1]) / 3
        for count, item in enumerate(self.board):
            # Fix for cases when 1 1 is 1 and 1 2 is two
            rows = item.sum() / 3
            board = self.board
            columns = board[:, count].sum() / 3
            if not item.prod() == 0:
                if rows == 1.0 or rows == 2.0:
                    return True
            if not board[:, count].prod(axis=0) == 0:
                if columns == 1.0 or columns == 2.0:
                    return True
        if not np.diag(self.board).prod() == 0:
            if diagonal_one == 1.0 or diagonal_one == 2.0:
                return True
        if not np.diag(self.board[::-1]).prod() == 0:
            if diagonal_two == 1.0 or diagonal_two == 2.0:
                return True
        return False

    def check_full(self):
        if 0 not in self.board:
            return True
        else:
            return False


def end_game():
    comfirmation = input("Want to repeat?([y]es or [n]o): ").lower()
    while (
        comfirmation != "yes"
        and comfirmation != "no"
        and comfirmation != "y"
        and comfirmation != "n"
    ):
        comfirmation = input("Want to repeat?([y]es or [n]o): ").lower()
    if comfirmation == "yes" or comfirmation == "y":
        board.reset()
        # So the player always start first
        return res_turn
    else:
        sys.exit(0)


def dislplay_formatted():
    for count, item in enumerate(board.display(), 1):
        print(item, end="")
        if count % 3 == 0:
            print()


# GAME


board = Board()
turn = deque([1, 2])
res_turn = deque([2, 1])

# LOOP
while True:
    # Display
    dislplay_formatted()
    # Display current player
    print(f"Your are player {turn[0]}")
    # Ask for Input
    while True:
        try:
            # Check the input
            prompt = list(map(int, input("Put in: ").split(" ")))
            if len(prompt) != 2:
                print("Input needs to be exactly 2 long")
                raise Exception
            if not 0 == board.board[prompt[0] - 1, prompt[1] - 1]:
                print("Occupied")
                raise Exception
            if 0 > prompt[0] > 2 or 0 > prompt[1] > 2:
                print("Invalid coordinate")
                raise Exception
        except Exception:
            print("Invalid input")
        else:
            break
    # Insert Input
    board.insert(prompt, turn[0])
    if board.check_win():
        print(f"Player {turn[0]} wins")
        dislplay_formatted()
        turn = end_game()
    if board.check_full():
        print("Tie")
        dislplay_formatted()
        turn = end_game()
    # TODO: Find if win state
    # End turn
    turn.append(turn[0])
    turn.popleft()
