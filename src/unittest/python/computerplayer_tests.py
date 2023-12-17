import unittest
from player import ComputerPlayer
from board import Board

class TestComputerPlayer(unittest.TestCase):

    def setUp(self):
        self.player = ComputerPlayer("X")
        self.opponent = ComputerPlayer("O")
        self.board = Board()

    def test_make_move_first_round(self):
        self.player.make_move(self.board, 0)
        self.assertEqual(self.board.game_grid[0][0], "X")

    def test_check_rows_no_winning_move(self):
        self.board.game_grid = [["X", "O", " "],
                                ["O", "O", "X"],
                                ["O", "X", "O"]]
        self.assertFalse(self.player.check_rows(self.board, "X"))

    def test_check_rows_winning_move(self):
        self.board.game_grid = [["X", "O", "X"],
                                ["O", "X", "O"],
                                ["O", "O", " "]]
        self.assertTrue(self.player.check_rows(self.board, "O"))

    def test_check_columns_no_winning_move(self):
        self.board.game_grid = [["X", "O", "X"],
                                ["O", "X", "O"],
                                [" ", "X", "O"]]
        self.assertFalse(self.player.check_columns(self.board, "X"))

    def test_check_columns_winning_move(self):
        self.board.game_grid = [["X", "O", " "],
                                ["O", "X", "O"],
                                ["O", "X", "O"]]
        self.assertTrue(self.player.check_columns(self.board, "O"))

    def test_check_diagonals_no_winning_move(self):
        self.board.game_grid = [["X", "O", "X"],
                                ["O", "X", "O"],
                                ["O", " ", "O"]]
        self.assertFalse(self.player.check_diagonals(self.board, "X"))

    def test_check_diagonals_winning_move(self):
        self.board.game_grid = [["X", "O", " "],
                                ["O", "O", "O"],
                                ["O", "X", "O"]]
        self.assertTrue(self.player.check_diagonals(self.board, "O"))

    def test_make_fallback_move_center_available(self):
        self.board.game_grid = [["X", "O", "X"],
                                ["O", " ", "O"],
                                ["O", "X", "O"]]
        self.player.make_fallback_move(self.board)
        self.assertEqual(self.board.game_grid[1][1], "X")

    def test_make_fallback_move_corner_available(self):
        self.board.game_grid = [["X", "O", "X"],
                                ["O", "X", "O"],
                                [" ", "X", "O"]]
        self.player.make_fallback_move(self.board)
        self.assertEqual(self.board.game_grid[0][0], "X")

    def test_make_fallback_move_side_available(self):
        self.board.game_grid = [["X", "O", "X"],
                                [" ", "X", "O"],
                                ["O", "X", "O"]]
        self.player.make_fallback_move(self.board)
        self.assertEqual(self.board.game_grid[1][0], "Fail")

if __name__ == '__main__':
    unittest.main()