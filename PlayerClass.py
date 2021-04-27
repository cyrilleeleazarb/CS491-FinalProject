# Player class
class Player:
    def __init__(self, player):
        # 'X' or 'O'
        self.player = player

    # Set player as player 'X' or player 'O'
    def set_player(self, player):
        self.player = player

    def get_player(self):
        return self.player

    def mark_square(self, column, row, currentboard):

        if currentboard[row][column] == '-':
            currentboard[row][column] = self.player
            return True
        else:
            return False