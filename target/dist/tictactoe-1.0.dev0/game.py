from board import Board
from player import HumanPlayer, ComputerPlayer

class Game:
    """
    Represents a tic-tac-toe game.

    Attributes:
    - board: The game board.
    - player: The human player.
    - computer: The computer player.
    - round: The current round number.
    """

    def __init__(self):
        """
        Initializes a new game of tic-tac-toe.

        The game consists of a board, a human player, a computer player,
        and a round counter. The human player uses 'O' as their symbol,
        while the computer player uses 'X'. The human player and the
        computer player are set as opponents of each other.

        Parameters:
        None

        Returns:
        None
        """
        self.board = Board()
        self.player = HumanPlayer('O')
        self.computer = ComputerPlayer('X')
        self.player.set_opponent(self.computer)
        self.computer.set_opponent(self.player)
        self.round = 0

    def run_round(self, player):
        """
        Runs a round of the game.

        Parameters:
        - player: The player who will make a move.

        Returns:
        None
        """
        player.make_move(self.board, self.round)
        self.board.check_winner()
        self.board.print_board()

    def run_game(self):
        """
        Runs the tic-tac-toe game until there is a winner or a tie.

        Returns:
        None
        """
        while self.board.winner is None:
            self.run_round(self.computer)
            if self.board.winner is not None:
                break
            self.run_round(self.player)
            self.round += 1

        if self.board.winner == 'tie':
            print("It's a tie!")
        else:
            if self.board.winner == self.computer.symbol:
                print("Computer wins! Muhahahaha! You will never beat me!")
            else:
                print(self.board.winner + " wins!")