import unittest
from unittest.mock import patch
from mockito import when, verify, mock
from game import Game
import app

class TestGame(unittest.TestCase):
    def test_game_instance_creation(self):
        game = Game()
        self.assertIsInstance(game, Game)

    @patch('app.Game.run_game')
    def test_run_game(self, mock_run_game):
        game = Game()
        game.run_game()
        mock_run_game.assert_called_once()
    
    def test_run_round(self):
        game = Game()
        game.board = mock()
        game.player = mock()
        game.computer = mock()
        game.run_round(game.player)
        verify(game.board).check_winner()
    
    def test_run_round_computer(self):
        game = Game()
        game.board = mock()
        game.player = mock()
        game.computer = mock()
        game.run_round(game.computer)
        verify(game.board).check_winner()

if __name__ == '__main__':
    unittest.main()