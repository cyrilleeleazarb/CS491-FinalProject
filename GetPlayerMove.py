class GetMoves():

    def get_player_move(self, player, board):
        board.display_board()

        row, col = input("Player " + str(player) + " please enter your move (row, col): ").split(', ')

        return row, col

    def correct_move_error(self):
        row, col = input("Selection not available, please enter a valid move: ").split(', ')

        return row, col


# Used for testing of PlayGamesClass object
class MockGetMoves():
    def __init__(self):
        self.move_count = -1
        self.row = []
        self.col = []

    def set_move(self, row, col, move_num):
        self.row.append(row)
        self.col.append(col)


    def get_player_move(self, player, board):
        self.move_count += 1
        return self.row[self.move_count], self.col[self.move_count]


    def correct_move_error(self, row, col):
        return row, col