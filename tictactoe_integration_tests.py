import unittest
import BoardClass
import PlayGameClass
import GetPlayerMove

class TestBoardWithPlayer(unittest.TestCase):

    def testSetPlayer(self):
        board = BoardClass.Board()
        board.set_current_player('O')
        self.assertEqual(board.get_current_player(), 'O')

    def testPlayerMark(self):
        board = BoardClass.Board()
        val = board.currentPlayer.mark_square(1, 2, board.board)
        self.assertEqual(val, True)


# PlayGame Class has_winner function test
# Test how it interacts with the board
class TestPlayGameHasWinner(unittest.TestCase):
    def test_HorizontalWinner(self):
        board = PlayGameClass.PlayGame()

        board.board.board[0][0] = 'X'
        board.board.board[0][1] = 'X'
        board.board.board[0][2] = 'X'

        self.assertEqual(True, board.has_winner())

    def test_VerticalWinner(self):
        board = PlayGameClass.PlayGame()

        board.board.board[0][0] = 'X'
        board.board.board[1][0] = 'X'
        board.board.board[2][0] = 'X'

        self.assertEqual(True, board.has_winner())

    def test_DiagonalWinner(self):
        board = PlayGameClass.PlayGame()

        board.board.board[0][0] = 'X'
        board.board.board[1][1] = 'X'
        board.board.board[2][2] = 'X'

        self.assertEqual(True, board.has_winner())

    def test_NoWinnerEmptyBoard(self):
        board = PlayGameClass.PlayGame()

        self.assertEqual(False, board.has_winner())

    def test_NoWinnerTie(self):
        board = PlayGameClass.PlayGame()

        board.board.board[0][0] = 'X'
        board.board.board[0][1] = 'O'
        board.board.board[0][2] = 'X'
        board.board.board[1][0] = 'X'
        board.board.board[1][1] = 'O'
        board.board.board[1][2] = 'O'
        board.board.board[2][0] = 'O'
        board.board.board[2][1] = 'X'
        board.board.board[2][2] = 'O'

        self.assertEqual(False, board.has_winner())

# Player Class mark_square function test
class TestPlayerClassMarkSquare(unittest.TestCase):

    def test_markSquareValidMoves(self):
        testBoard = BoardClass.Board()
        result = True

        for i in range(3):
            for j in range(3):
                self.assertEqual(result, testBoard.currentPlayer.mark_square(i, j, testBoard.board))

    def test_markSquareInvalidMoves(self):
        testBoard = BoardClass.Board()

        for i in range(3):
            for j in range(3):
                testBoard.board[i][j] = 'X'

        result = False

        for i in range(3):
            for j in range(3):
                self.assertEqual(result, testBoard.currentPlayer.mark_square(i, j, testBoard.board))


class TestPlayGame(unittest.TestCase):
    def test_play_game(self):
        player_move_test = GetPlayerMove.MockGetMoves()
        play_game_test = PlayGameClass.PlayGame()
        player_move_test.set_move(0, 0, 0)
        player_move_test.set_move(1, 2, 1)
        player_move_test.set_move(1, 1, 2)
        player_move_test.set_move(0, 1, 3)
        player_move_test.set_move(2, 2, 4)
        player_move_test.set_move(0, 2, 5)

        self.assertEqual('X', play_game_test.play_game(player_move_test))


if __name__ == "__main__":
    unittest.main()