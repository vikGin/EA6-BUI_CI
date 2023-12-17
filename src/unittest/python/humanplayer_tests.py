import unittest
from mockito import when
from player import HumanPlayer
from board import Board

class TestHumanPlayer(unittest.TestCase):
    def test_make_move_valid_input(self):
        player = HumanPlayer('X')
        board = Board()
        move_input = '1,2'  # Valid input
        expected_row = 0
        expected_col = 1

        # Mocking the input function to simulate user input
        when('builtins').input().thenReturn(move_input)

        player.make_move(board, 1)

        self.assertEqual(board.game_grid[expected_row][expected_col], 'X')

    def test_make_move_invalid_input(self):
        player = HumanPlayer('X')
        board = Board()
        invalid_move_input = '4,2'  # Invalid input
        valid_move_input = '1,2'  # Valid input
        expected_row = 0
        expected_col = 1

        # Mocking the input function to simulate user input
        when('builtins').input().thenReturn(invalid_move_input).thenReturn(valid_move_input)

        player.make_move(board, 1)

        self.assertEqual(board.game_grid[expected_row][expected_col], 'X')

if __name__ == '__main__':
    unittest.main()