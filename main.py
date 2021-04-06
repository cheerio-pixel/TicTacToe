import numpy as np


## BOARD
class Board:
    def __init__(self):
        self.board = np.zeros((3, 3))

    def insert(self, x, y, player):
        x -= 1
        y -= 1
        if not 0 == self.board[x, y]:
            print("Occupied")
            return
        if player != 1 and player != 2:
            print("Invalid player")
            return
        if 0 > x > 2 or 0 > y > 2:
            print("Invalid coordinate")
            return
        else:
            self.board[x, y] = player

    def display(self):
        for item in self.board:
            for second_item in item:
                if second_item == 0:
                    print("[ ]", end="")
                if second_item == 1:
                    print("[X]", end="")
                if second_item == 2:
                    print("[O]", end="")
            print()

    def reset(self):
        self.board = np.zeros((3, 3))


## GAME
board = Board()
board.insert(
    x=1,
    y=2,
    player=1,
)

board.insert(x=2, y=2, player=2)
board.display()
