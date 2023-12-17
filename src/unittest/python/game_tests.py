import unittest
from game import Game
from board import Board
from player import HumanPlayer, ComputerPlayer

class TestGame(unittest.TestCase):

    def test_run_round(self):
        game = Game()
        game.board = Board()
        game.player = HumanPlayer('O')
        game.computer = ComputerPlayer('X')

        # Test when player is the computer
        game.run_round(game.computer)
        self.assertEqual(game.board.winner, None)

        # Test when winning move is made
        game.board.game_grid = [['X', 'O', 'X'],
                                ['O', 'X', 'O'],
                                ['O', 'O', 'X']]
        game.run_round(game.computer)
        self.assertEqual(game.board.winner, game.computer.symbol)


    def test_run_game(self):
        game = Game()
        game.board = Board()
        game.player = HumanPlayer('O')
        game.computer = ComputerPlayer('X')

        # Test when there is a tie
        game.board.winner = 'tie'
        game.run_game()
        self.assertEqual(game.board.winner, 'tie')

        # Test when computer wins
        game.board.winner = game.computer.symbol
        game.run_game()
        self.assertEqual(game.board.winner, game.computer.symbol)

        # Test when human wins
        game.board.winner = game.player.symbol
        game.run_game()
        self.assertEqual(game.board.winner, game.player.symbol)

if __name__ == '__main__':
    unittest.main()