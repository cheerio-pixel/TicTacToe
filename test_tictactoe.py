import tictactoe as sut


def two_players():
    return sut.Player("X"), sut.Player("O")


def eigth_boards():
    board1 = sut.TicTacToeBoard()
    board2 = sut.TicTacToeBoard()
    board3 = sut.TicTacToeBoard()
    board4 = sut.TicTacToeBoard()
    board5 = sut.TicTacToeBoard()
    board6 = sut.TicTacToeBoard()
    board7 = sut.TicTacToeBoard()
    board8 = sut.TicTacToeBoard()
    for x in range(3):
        board1.board[x][0] = "X"
        board2.board[x][1] = "X"
        board3.board[x][2] = "X"
        board4.board[0][x] = "X"
        board5.board[1][x] = "X"
        board6.board[2][x] = "X"
    for x, y in zip(range(3), reversed(range(3))):
        board7.board[x][y] = "X"
        board8.board[y][x] = "X"
    return (board1, board2, board3, board4, board5, board6, board7, board8)


class TestPlayer:
    def test_init(self):
        player = sut.Player("X")
        assert player.symbol == "X"


class TestTurn:
    class TestEnqueue:
        def test_turn_list(self):
            turn = sut.Turn()
            player1, player2 = two_players()
            turn.enqueue(player1)
            turn.enqueue(player2)
            assert turn.turn_list == [player1, player2]

        def test_multiple_enqueues(self):
            turn = sut.Turn()
            player1, player2 = two_players()
            turn.enqueue(player1, player2)
            assert turn.turn_list == [player1, player2]

    def test_nxt(self):
        turn = sut.Turn()
        turn.enqueue(*two_players())
        turn.nxt()
        assert turn.point == 1
        turn.nxt()
        assert not turn.point == 2


class TestTicTacToeBoard:
    def test_make_board(self):
        board = sut.TicTacToeBoard()
        assert board.board == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_get_diag(self):
        board = sut.TicTacToeBoard()
        for x in range(3):
            board.board[x][x] = "X"
        assert board.get_diag() == ["X", "X", "X"]
        for x, y in zip(range(3), reversed(range(3))):
            board.board[x][y] = "O"
        assert board.get_diag(True) == ["O", "O", "O"]

    def test_check_line(self):
        board = sut.TicTacToeBoard()
        for x in range(3):
            board.board[1][x] = "X"
        assert board.check_line(board.board[1], "X")
        board.board[1][2] = 0
        assert not board.check_line(board.board[1], "X")

    def test_check_lines(self):
        board = sut.TicTacToeBoard()
        for x in range(3):
            board.board[x][0] = "X"
        assert board.check_lines("X")
        assert not board.check_lines("O")

    def test_win(self):
        for x in eigth_boards():
            assert x.win("X")
