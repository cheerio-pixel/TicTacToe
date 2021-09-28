# * Imports

import pygame
import math

# * Logic


class Turn:
    def __init__(self):
        self.array = []
        self.point = 0

    def append(self, thing):
        self.array.append(thing)

    def get_list(self):
        return self.array

    def get_point(self):
        return self.point

    def set_point(self, point):
        self.point = point

    def has_player(self, player):
        return player in self.get_list()

    def enqueue_player(self, player):
        if (not self.has_player(player)) and Player.is_player(player):
            self.append(player)

    def enqueue_players(self, *args):
        for e in args:
            self.enqueue_player(e)

    def next(self):
        if not self.get_point() + 1 >= len(self.get_list()):
            self.set_point(self.get_point() + 1)

    def current_turn(self):
        return self.get_list()[self.get_point()]


class Board:
    def __init__(self, dimensions: list):
        "Board of a tic tac toe game"
        self.dimensions = dimensions
        self.clear_board()

    def set_board(self, board: list):
        self.board = board

    def get_board(self):
        return self.board

    def get_dimensions(self):
        return self.dimensions

    @classmethod
    def empty_board(cls, dimensions: list):
        final = []
        for _ in range(math.prod(dimensions)):
            final.append(0)
        return final

    def coords_to_index(self, x: int, y: int):
        x, y = x - 1, y - 1
        return x + self.get_dimensions()[0] * y

    def insert(self, x: int, y: int, symbol: str):
        dimensions = self.get_dimensions()
        exceptions = [
            Exception(x)
            for x in [
                "x coordinate is too big",
                "y coordinate is too big",
                "x coordinate is too small ",
                "y coordinate is too small",
            ]
        ]
        cases = [
            dimensions[0] < x,
            dimensions[1] < y,
            0 > x,
            0 > y,
        ]
        for c, e in zip(cases, exceptions):
            if c:
                raise e
        self.get_board()[self.coords_to_index(x, y)] = symbol

    def clear_board(self):
        self.set_board(Board.empty_board(self.dimensions))

    # Check if win
    def check_lines(
        self, symbol: str, is_vertical: bool, sdimensions: list, sboard: list
    ):
        board = sboard
        dimensions = sdimensions
        is_win = True
        for y in range(0, dimensions[0]):
            for x in range(1, dimensions[1]):
                if (
                    symbol
                    != board[
                        self.coords_to_index(y, x)
                        if is_vertical
                        else self.coords_to_index(x, y)
                    ]
                ):
                    is_win = False
                    break
            if is_win:
                return is_win
            is_win = True
        return False

    def get_diag(self, board):
        return [
            board[self.coords_to_index(i, i)]
            for i in range(self.get_dimensions()[0])
        ]

    def check_diag(self, symbol: str, reverse: bool):
        return self.check_lines(
            symbol,
            False,
            [0, 1],
            self.get_diag(self.get_board()[::-1])
            if reverse
            else self.get_diag(self.get_board()),
        )

    def win(self, symbol: str):
        return (
            self.check_diag(symbol, False)
            or self.check_diag(symbol, True)
            or self.check_lines(
                symbol, False, self.get_dimensions(), self.get_board()
            )
            or self.check_lines(
                symbol, True, self.get_dimensions(), self.get_board()
            )
        )


class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol[0]

    def get_player(self):
        return self.symbol

    @classmethod
    def is_player(cls, player):
        return isinstance(player, Player)


class Game:
    pass


# * Gui
