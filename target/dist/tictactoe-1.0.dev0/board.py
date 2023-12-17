class Board:
    """
    Represents a tic-tac-toe game board.

    Attributes:
    - game_grid: A 2D list representing the game grid.
    - winner: A string representing the winner of the game ('X', 'O', 'tie', or None).
    """
    def __init__(self):
        """
        Initializes a new instance of the Game class.
        """
        self.game_grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.winner = None

    def is_empty(self, row, col):
        """
        Check if a specific cell in the game grid is empty.

        Parameters:
        - row (int): The row index of the cell.
        - col (int): The column index of the cell.

        Returns:
        - bool: True if the cell is empty, False otherwise.
        """
        return self.game_grid[row][col] == ' '

    def print_board(self):
            """
            Prints the current game board.
            """
            print("-------------")
            for row in self.game_grid:
                print("| " + " | ".join(row) + " |")
                print("-------------")

    def check_winner(self):
        """
        Checks if there is a winner in the tic-tac-toe game.

        The function checks the rows, columns, and diagonals of the game grid
        to determine if there is a winning player. If a winner is found, the
        `self.winner` attribute is updated with the winning player's symbol.

        Returns:
            None
        """
        # Check rows
        for row in self.game_grid:
            if row[0] == row[1] == row[2] != ' ':
                self.winner = row[0]
                return

        # Check columns
        for col in range(3):
            if self.game_grid[0][col] == self.game_grid[1][col] == self.game_grid[2][col] != ' ':
                self.winner = self.game_grid[0][col]
                return

        # Check diagonals
        if self.game_grid[0][0] == self.game_grid[1][1] == self.game_grid[2][2] != ' ':
            self.winner = self.game_grid[0][0]
            return
        if self.game_grid[0][2] == self.game_grid[1][1] == self.game_grid[2][0] != ' ':
            self.winner = self.game_grid[0][2]
            return

        # Check for tie
        if all(cell != ' ' for row in self.game_grid for cell in row):
            self.winner = 'tie'
