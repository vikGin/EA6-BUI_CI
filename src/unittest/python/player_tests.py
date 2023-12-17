import unittest
from player import Player

class PlayerTests(unittest.TestCase):
    def test_init(self):
        player = Player("X")
        self.assertEqual(player.symbol, "X")
        self.assertIsNone(player.opponent)

    def test_set_opponent(self):
        player1 = Player("X")
        player2 = Player("O")
        player1.set_opponent(player2)
        self.assertEqual(player1.opponent, player2)

    def test_make_move(self):
        player = Player("X")
        board = [["", "", ""], ["", "", ""], ["", "", ""]]
        round_number = 1
        with self.assertRaises(NotImplementedError):
            player.make_move(board, round_number)

if __name__ == "__main__":
    unittest.main()