import numpy as np
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
        self.board = np.zeros((3, 3))


# GAME

board = Board()
turn = deque([1, 2])

# LOOP
while True:
    # Display
    for count, item in enumerate(board.display(), 1):
        print(item, end="")
        if count % 3 == 0:
            print()
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
            if not 0 == board.board[prompt[0], prompt[1]]:
                print("Occupied")
                raise Exception
            if 0 > prompt[0] > 2 or 0 > prompt[1] > 2:
                print("Invalid coordinate")
                raise Exception
        except:
            print("Invalid input")
        else:
            break
    # Insert Input
    board.insert(prompt, turn[0])
    # TODO: Find if win state
    # Find if win or full state
    # End turn
    turn.append(turn[0])
    turn.popleft()
