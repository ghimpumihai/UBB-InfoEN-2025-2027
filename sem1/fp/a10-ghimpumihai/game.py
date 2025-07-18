from board import Board

class ComputerStrategy:
    def __init__(self, board: Board, x: int, y: int):
        self.board = board
        self.x = x
        self.y = y
        self.computer_place()

    def computer_place(self):
            row = 6 - self.x
            column = 6 - self.y
            self.board.place_obstruction(row, column)

class Obstruction:
    def __init__(self, board: Board, row: int, column: int):
        self.__board = board
        self.strategy = ComputerStrategy(self.__board, row, column)

    @property
    def board(self):
        return self.__board