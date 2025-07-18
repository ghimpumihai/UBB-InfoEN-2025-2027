import unittest
from game import Obstruction, ComputerStrategy
from board import Board

class TestGame(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_obstruction_initialization(self):
        obstruction = Obstruction(self.board, 3, 3)
        self.assertIsInstance(obstruction, Obstruction)
        self.assertIsInstance(obstruction.strategy, ComputerStrategy)
        self.assertEqual(obstruction.strategy.x, 3)
        self.assertEqual(obstruction.strategy.y, 3)

    def test_place_player_obstruction(self):
        self.board.place_obstruction(2, 2)
        self.assertEqual(self.board.obstruction_board[2][2], 1)
        self.board.place_obstruction(4, 4)
        self.assertEqual(self.board.obstruction_board[4][4], 2)

if __name__ == '__main__':
    unittest.main()