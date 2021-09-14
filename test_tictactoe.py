import tictactoe as sut
import unittest


class TestTurnMethods(unittest.TestCase):
    def test_next(self):
        turn = sut.Turn()
        for i in ["a" "b"]:
            turn.append(i)
        for _ in range(len(turn.get_list())):
            turn.next()
        self.assertEqual(0, turn.get_point())

    def test_enqueue_player(self):
        turn = sut.Turn()
        turn.enqueue_player(sut.Player("X"))
        self.assertEqual(len(turn.get_list()), 1)

    def test_enqueue_players(self):
        turn = sut.Turn()
        turn.enqueue_players(sut.Player("X"), sut.Player("X"), sut.Player("X"))
        self.assertEqual(len(turn.get_list()), 3)


class TestBoardMethods(unittest.TestCase):
    def test_empty_board(self):
        self.assertEqual([0, 0, 0, 0], sut.Board.empty_board([2, 2]))

    def test_clear_board(self):
        board = sut.Board([2, 2])
        board.clear_board()
        self.assertEqual(board.get_board(), [0, 0, 0, 0])

    def test_insert(self):
        board = sut.Board([2, 3])
        board.insert(1, 1, "X")
        self.assertEqual(board.get_board(), ["X", 0, 0, 0, 0, 0])

    def test_check_lines_horizontal(self):
        board = sut.Board([3, 3])
        board.set_board([0, 0, 0, "X", "X", "X", 0, 0, 0])
        self.assertTrue(board.check_lines("X", False))

    def test_check_lines_vertical(self):
        board = sut.Board([3, 3])
        board.set_board(["X", 0, 0, "X", 0, 0, "X", 0, 0])
        self.assertTrue(board.check_lines("X", True))


if __name__ == "__main__":
    unittest.main()
