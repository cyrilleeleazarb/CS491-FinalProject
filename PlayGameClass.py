from BoardClass import Board
from GetPlayerMove import GetMoves

class PlayGame(object):

    def __init__(self):
        self.board = Board()
        self.move_input = GetMoves()

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game
        :return: ????
        """

        for i in range(3):
            # check horizontals
            if (self.board.board[i][0] == "X") and (self.board.board[i][1] == "X") and (self.board.board[i][2] == "X"):
                return True
            elif (self.board.board[i][0] == "O") and (self.board.board[i][1] == "O") and (self.board.board[i][2] == "O"):
                return True
            # check verticals
            elif (self.board.board[0][i] == "X") and (self.board.board[1][i] == "X") and (self.board.board[2][i] == "X"):
                return True
            elif (self.board.board[0][i] == "O") and (self.board.board[1][i] == "O") and (self.board.board[2][i] == "O"):
                return True

        # check diagonals
        if (self.board.board[0][0] == "X") and (self.board.board[1][1] == "X") and (self.board.board[2][2] == "X"):
            return True
        elif (self.board.board[0][0] == "O") and (self.board.board[1][1] == "O") and (self.board.board[2][2] == "O"):
            return True

        # if all else fails
        return False

    def play_game(self, move_input):

        while not self.has_winner():
            if self.board.currentPlayer == 'X':
                self.board.currentPlayer.set_player('O')
            else:
                self.board.currentPlayer.set_player('X')

            row, col = move_input.get_player_move(self.board.currentPlayer.player, self.board)


            # illegal move, re-prompt user
            while not self.board.currentPlayer.mark_square(int(col), int(row), self.board.board):
                row, col = move_input.correct_move_error()



        return self.board.currentPlayer.player

    def get_winner(self):
        winner = self.play_game(self.move_input)
        print("{} has won!".format(winner))
