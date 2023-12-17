import unittest
from mockito import mock, when, verify

from board import Board

class BoardTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_empty(self):
        self.assertTrue(self.board.is_empty(0, 0))
        self.board.game_grid[0][0] = 'X'
        self.assertFalse(self.board.is_empty(0, 0))

    # def test_print_board(self):
    #     with patch('builtins.print') as print_mock:
    #         self.board.print_board()

    #         # Verify that the print function was called with the expected output
    #         verify(print_mock).assert_called_with("-------------")
    #         verify(print_mock).assert_called_with("|   |   |   |")
    #         verify(print_mock).assert_called_with("-------------")

    def test_check_winner_row(self):
        self.board.game_grid[0] = ['X', 'X', 'X']
        self.board.check_winner()
        self.assertEqual(self.board.winner, 'X')

    def test_check_winner_column(self):
        self.board.game_grid[0][0] = 'O'
        self.board.game_grid[1][0] = 'O'
        self.board.game_grid[2][0] = 'O'
        self.board.check_winner()
        self.assertEqual(self.board.winner, 'O')

    def test_check_winner_diagonal(self):
        self.board.game_grid[0][0] = 'X'
        self.board.game_grid[1][1] = 'X'
        self.board.game_grid[2][2] = 'X'
        self.board.check_winner()
        self.assertEqual(self.board.winner, 'X')

    def test_check_winner_tie(self):
        self.board.game_grid = [['X', 'O', 'X'],
                                ['O', 'X', 'O'],
                                ['O', 'X', 'O']]
        self.board.check_winner()
        self.assertEqual(self.board.winner, 'tie')

if __name__ == '__main__':
    unittest.main()