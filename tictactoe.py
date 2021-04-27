""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming,
          and you make use of relevant object-oriented design principles.
"""

from PlayGameClass import PlayGame


class Board(object):

    def __init__(self):

        self.board = []

        for x in range(3):
            self.board.append([])
            for y in range(3):
                self.board[x].append("-")

        """
        Initializes the Board of size 3x3
        """

        pass

    def mark_square(self, column, row, player):

        if self.board[row][column] == '-':
            self.board[row][column] = player
            return True
        else:
            return False

        """
        Marks a square at coordinate (column, row) for player
        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square
        :return: ????
        """

        pass

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game
        :return: ????
        """

        for i in range(3):
            # check horizontals
            if (self.board[i][0] == "X") and (self.board[i][1] == "X") and (self.board[i][2] == "X"):
                return True
            elif (self.board[i][0] == "O") and (self.board[i][1] == "O") and (self.board[i][2] == "O"):
                return True
            # check verticals
            elif (self.board[0][i] == "X") and (self.board[1][i] == "X") and (self.board[2][i] == "X"):
                return True
            elif (self.board[0][i] == "O") and (self.board[1][i] == "O") and (self.board[2][i] == "O"):
                return True

        # check diagonals
        if (self.board[0][0] == "X") and (self.board[1][1] == "X") and (self.board[2][2] == "X"):
            return True
        elif (self.board[0][0] == "O") and (self.board[1][1] == "O") and (self.board[2][2] == "O"):
            return True

        # if all else fails
        return False

    def display_board(self):
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print()

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        :return: (str) the letter representing the player who won
        """

        player = 'O'

        while not self.has_winner():
            if player == 'X':
                player = 'O'

            else:
                player = 'X'

            self.display_board()
            row, col = input("Player " + str(player) + " please enter your move (row, col): ").split(', ')

            # if illegal move, reprompt
            while not self.mark_square(int(col), int(row), player):
                row, col = input("Selection not available, please enter a valid move: ").split(', ')

            self.display_board()

        return player


if __name__ == '__main__':
    game = PlayGame()
    game.get_winner()
    # board = Board()
    # winner = board.play_game()
    # print("{} has won!".format(winner))