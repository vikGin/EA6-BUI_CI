class Player:
    """
    Represents a player in the tic-tac-toe game.

    Attributes:
        symbol (str): The symbol representing the player on the game board.
        opponent (Player): The opponent player.
    """

    def __init__(self, symbol):
        """
        Initializes a new instance of the Game class.

        Args:
            symbol (str): The symbol representing the player.

        Attributes:
            symbol (str): The symbol representing the player.
            opponent (None): The opponent player.

        Returns:
            None
        """
        self.symbol = symbol
        self.opponent = None

    def set_opponent(self, opponent):
        """
        Sets the opponent player.

        Args:
            opponent (Player): The opponent player.
        """
        self.opponent = opponent

    def make_move(self, board, round):
        """
        Makes a move on the game board.

        This method should be overridden in child classes.

        Args:
            board (list): The game board.
            round (int): The current round number.
        """
        raise NotImplementedError("This method should be overridden in child classes")

class HumanPlayer(Player):
    """
    Represents a human player in the tic-tac-toe game.

    Attributes:
    - symbol: The symbol representing the player on the game board.
    """

    def make_move(self, board, round):
        """
        Makes a move on the game board based on user input.

        Args:
            board (Board): The game board.
            round (int): The current round number.

        Returns:
            None
        """
        while True:
            print("Enter the coordinates of your move: ")
            move = input()
            if len(move) != 3 or move[1] != ',':
                print("Invalid input. Input should be two numbers separated by a comma.")
            elif move[0] not in ['1', '2', '3'] or move[2] not in ['1', '2', '3']:
                print("Invalid input. Input should be two numbers between 1 and 3 separated by a comma.")
            else:
                row = int(move[0]) - 1
                col = int(move[2]) - 1
                if not board.is_empty(row, col):
                    print("Space already occupied. Try again.")
                else:
                    board.game_grid[row][col] = self.symbol
                    break

class ComputerPlayer(Player):
    """
    Represents a computer player in the tic-tac-toe game.

    Attributes:
        symbol (str): The symbol representing the computer player on the game board.
        opponent (Player): The opponent player.
    """
    def make_move(self, board, round):
        """
        Makes a move for the player based on the current round.

        Args:
            board (Board): The game board.
            round (int): The current round number.

        Returns:
            None
        """
        if round == 0:
            board.game_grid[0][0] = self.symbol
        elif round == 1:
            self.make_second_move(board)
        elif round >= 2:
            if not self.make_winning_move(board) and not self.make_blocking_move(board):
                self.make_fallback_move(board)

    def make_second_move(self, board):
        """
        Makes the second move for the player.

        Args:
            board (Board): The game board.

        Returns:
            None
        """
        if board.game_grid[1][1] == self.opponent.symbol:
            board.game_grid[2][2] = self.symbol
        else:
            if board.is_empty(0, 1) and board.is_empty(0, 2):
                board.game_grid[0][2] = self.symbol
            else:
                board.game_grid[2][0] = self.symbol

    def make_winning_move(self, board):
        """
        Checks if there is a winning move for the current player on the board.

        Args:
            board (list): The game board.

        Returns:
            bool: True if there is a winning move, False otherwise.
        """
        return self.check_rows(board, self.symbol) or \
               self.check_columns(board, self.symbol) or \
               self.check_diagonals(board, self.symbol)

    def make_blocking_move(self, board):
        """
        Makes a blocking move on the board to prevent the opponent from winning.

        Args:
            board (list): The current state of the game board.

        Returns:
            bool: True if a blocking move is made, False otherwise.
        """
        return self.check_rows(board, self.opponent.symbol) or \
               self.check_columns(board, self.opponent.symbol) or \
               self.check_diagonals(board, self.opponent.symbol)

    def check_rows(self, board, symbol):
        """
        Check if there are any rows in the game grid that have two occurrences of the given symbol.
        If such a row is found, mark the empty cell in that row with the symbol and return True.
        If no such row is found, return False.

        Args:
            board (Board): The game board object.
            symbol (str): The symbol to check for.

        Returns:
            bool: True if a row with two occurrences of the symbol is found and marked, False otherwise.
        """
        for row in range(len(board.game_grid)):
            if [cell for cell in board.game_grid[row]].count(symbol) == 2:
                for col in range(len(board.game_grid[row])):
                    if board.is_empty(row, col):
                        board.game_grid[row][col] = self.symbol
                        return True
        return False

    def check_columns(self, board, symbol):
        """
        Check if there are any columns with two occurrences of the given symbol.
        
        Args:
            board (Board): The game board.
            symbol (str): The symbol to check for.
        
        Returns:
            bool: True if a move was made, False otherwise.
        """
        for col in range(len(board.game_grid[0])):
            column = [board.game_grid[row][col] for row in range(len(board.game_grid))]
            if column.count(symbol) == 2:
                for row in range(len(column)):
                    if board.is_empty(row, col):
                        board.game_grid[row][col] = self.symbol
                        return True
        return False

    def check_diagonals(self, board, symbol):
        """
        Check the diagonals of the game board for a given symbol.

        Args:
            board (Board): The game board.
            symbol (str): The symbol to check for.

        Returns:
            bool: True if a move was made, False otherwise.
        """
        diagonals = [[board.game_grid[i][i] for i in range(len(board.game_grid))],
                     [board.game_grid[i][len(board.game_grid)-i-1] for i in range(len(board.game_grid))]]
        for i, diagonal in enumerate(diagonals):
            if diagonal.count(symbol) == 2:
                for j in range(len(diagonal)):
                    if board.is_empty(j, j if i == 0 else len(board.game_grid)-j-1):
                        board.game_grid[j][j if i == 0 else len(board.game_grid)-j-1] = self.symbol
                        return True
        return False

    def make_fallback_move(self, board):
        """
        Makes a fallback move on the board if no winning or blocking move is available.

        Args:
            board (Board): The game board.

        Returns:
            None
        """
        # If no winning or blocking move, play in center if available
        if board.is_empty(1, 1):
            board.game_grid[1][1] = self.symbol
        else:
            # Play in a corner if available
            if board.is_empty(0, 0):
                board.game_grid[0][0] = self.symbol
            elif board.is_empty(0, 2):
                board.game_grid[0][2] = self.symbol
            elif board.is_empty(2, 0):
                board.game_grid[2][0] = self.symbol
            elif board.is_empty(2, 2):
                board.game_grid[2][2] = self.symbol
            else:
                # Play in a side if available
                if board.is_empty(0, 1):
                    board.game_grid[0][1] = self.symbol
                elif board.is_empty(1, 0):
                    board.game_grid[1][0] = self.symbol
                elif board.is_empty(1, 2):
                    board.game_grid[1][2] = self.symbol
                elif board.is_empty(2, 1):
                    board.game_grid[2][1] = self.symbol
