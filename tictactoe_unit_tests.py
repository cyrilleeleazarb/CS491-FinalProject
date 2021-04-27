import unittest
import BoardClass
import PlayerClass
import PlayGameClass

# Board Class constructor test
class TestBoardClassConstructor(unittest.TestCase):

    def test_checkColumns(self):
        testBoard = BoardClass.Board()
        self.assertEqual(3, len(testBoard.board))

    def test_checkRows(self):
        testBoard = BoardClass.Board()
        self.assertEqual(3, len(testBoard.board[0]))

    def test_checkBoardIsBlank(self):
        testBoard = BoardClass.Board()

        for i in testBoard.board:
            for j in i:
                self.assertEqual("-", j)


class TestBoardModifiers(unittest.TestCase):
    def test_get_player(self):
        board_test = BoardClass.Board()
        board_test.set_current_player('X')

        self.assertEqual('X', board_test.get_current_player())

class TestPlayerModifiers(unittest.TestCase):
    def test_player_constructor(self):
        player_test = PlayerClass.Player('X')

        self.assertEqual('X', player_test.get_player())

    def test_player_setter(self):
        player_test = PlayerClass.Player('X')
        player_test.set_player('Y')

        self.assertEqual('Y', player_test.get_player())

if __name__ == "__main__":
    unittest.main()