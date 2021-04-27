from PlayerClass import Player

class Board(object):

    def __init__(self):

        self.board = []
        self.currentPlayer = Player('O')

        for x in range(3):
            self.board.append([])
            for y in range(3):
                self.board[x].append("-")

        """
        Initializes the Board of size 3x3
        """

    def set_current_player(self, current_player):
        self.currentPlayer = current_player

    def get_current_player(self):
        return self.currentPlayer

    def display_board(self):
        for i in self.board:
            for j in i:
                print(j, end = "")
            print()