from typing import Union
from pyglet import window, shapes, graphics, gui
import pyglet
from pyglet.window import key
import sys


class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol


class Turn:
    def __init__(self):
        self.turn_list = []
        self.point = 0

    def enqueue(self, *players: Player) -> None:
        for player in players:
            if (player not in self.turn_list) and (isinstance(player, Player)):
                self.turn_list.append(player)

    def nxt(self) -> None:
        if self.point < len(self.turn_list) - 1:
            self.point += 1
        else:
            self.point = 0

    def current(self) -> Player:
        return self.turn_list[self.point]


class TicTacToeBoard:
    def __init__(self):
        self.board = self.make_board()

    def make_board(self) -> list[list[Union[int, str]]]:
        result = []
        for _ in range(3):
            result.append([0, 0, 0])
        return result

    def get_diag(self, is_reverse: bool = False) -> list:
        temp_board = self.board[::-1] if is_reverse else self.board
        result = []
        for i in range(3):
            result.append(temp_board[i][i])
        return result

    def check_line(self, line, symbol: str) -> bool:
        # This is assuming that we are using
        return len(line) == line.count(symbol)

    def check_lines(self, symbol: str) -> bool:
        temp_board = self.board
        vertical_temp_board = zip(*self.board[::-1])
        for l, i in zip(temp_board, vertical_temp_board):
            if self.check_line(l, symbol) or self.check_line(i, symbol):
                return True
        return False

    def check_diag(self, symbol: str) -> bool:
        for x in range(2):
            if self.check_line(self.get_diag(bool(x)), symbol):
                return True
        return False

    def win(self, symbol: str) -> bool:
        return self.check_lines(symbol) or self.check_diag(symbol)


class Game:
    """Tic-Tac-Toe Game class
    This class compose turn and board to make
    a game of tic-tac-toe
    Args:
        turn (Turn): A Turn object holding players
        board (Board): A Board object having a list
    """

    def __init__(self, turn: Turn, board: TicTacToeBoard):
        self.turn = turn
        self.board = board

    def ask_input(self):
        """In case of invalid input, this function is going to be called again
        so be sure to have clean the input queue by then
        """
        inp = (0, 0)
        return inp

    def is_insert_input(self, inp: tuple[int, int]) -> bool:
        "Safeguard before inserting input"
        if 2 == len(
            list(
                filter(lambda x: x < 0 and x > len(self.board.board) - 1, inp)
            )
        ):
            return True
        elif self.board.board[inp[0]][inp[1]] == 0:
            return True
        else:
            return False

    def insert_input(self, inp: tuple[int, int], player: Player) -> None:
        self.board.board[inp[0]][inp[1]] = player.symbol

    def ask_win(self, board: TicTacToeBoard, player: Player) -> bool:
        return board.win(player.symbol)

    def play(self):
        current_turn = self.turn.current()
        current_input = self.ask_input()
        while not self.is_insert_input(current_input):
            current_input = self.ask_input()
        self.insert_input(current_input, current_turn)
        is_win = self.ask_win(self.board, current_turn)
        self.turn.nxt()
        return is_win

    def play_loop(self):
        while not self.play():
            continue


class TerminalReplGame(Game):
    def print_game(self):
        for x in self.board.board:
            print(x)

    def ask_input(self):
        inp = input("INPUT(Example 1 2): ")
        if inp == "exit":
            raise SystemExit(1)
        result = inp.split(" ")
        return tuple(map(lambda x: x - 1, map(int, result)))

    def play_loop(self):
        self.print_game()
        while not self.play():
            self.print_game()


class Square(shapes.BorderedRectangle):
    def __init__(
        self,
        x,
        y,
        width,
        border=1,
        color=(255, 255, 255),
        border_color=(100, 100, 100),
        batch=None,
        group=None,
    ):
        super().__init__(
            x,
            y,
            width,
            width,
            border=border,
            color=color,
            border_color=border_color,
            batch=batch,
            group=group,
        )


class Cross(shapes.Line):
    def __init__(self, x, y, x2, y2, width, color, batch, group):
        super().__init__(
            x, y, x2, y2, width=width, color=color, batch=batch, group=group
        )
        super().__init__(
            x, y2, x2, y, width=width, color=color, batch=batch, group=group
        )


class PygletGameWindow(Game, pyglet.window.Window):
    def __init__(
        self,
        turn: Turn,
        board: TicTacToeBoard,
        width=None,
        height=None,
        caption=None,
        resizable=False,
        style=None,
        fullscreen=False,
        visible=True,
        vsync=True,
        file_drops=False,
        display=None,
        screen=None,
        config=None,
        context=None,
        mode=None,
    ):
        super().__init__(turn, board)
        super(pyglet.window.Window, self).__init__(
            width=width,
            height=height,
            caption=caption,
            resizable=resizable,
            style=style,
            fullscreen=fullscreen,
            visible=visible,
            vsync=vsync,
            file_drops=file_drops,
            display=display,
            screen=screen,
            config=config,
            context=context,
            mode=mode,
        )
        self.square_batch: graphics.Batch = graphics.Batch()
        self.square_buttons: graphics.Batch = graphics.Batch()
        self.inp = ()

    def read_board(self):
        # Make square objects based on board
        pass

    def ask_input(self):
        # Get input
        # Let a variable, b, be that input
        # Clean input
        return self.inp  # Return b

    def on_draw(self):
        self.clear()
        self.square_batch.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        self.inp = (x, y)
        print(self.inp)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            return


if __name__ == "__main__":
    turn = Turn()
    player1 = Player("X")
    player2 = Player("O")
    turn.enqueue(player1, player2)
    tic_tac_toe_board = TicTacToeBoard()

    if sys.argv[1] == "terminal":
        terminal_game = TerminalReplGame(
            turn=turn,
            board=tic_tac_toe_board,
        )
        terminal_game.play_loop()
    if sys.argv[1] == "pyglet":
        pyglet_game = PygletGameWindow(
            turn=turn,
            board=tic_tac_toe_board,
            width=640,
            height=480,
        )
        pyglet.app.run()
