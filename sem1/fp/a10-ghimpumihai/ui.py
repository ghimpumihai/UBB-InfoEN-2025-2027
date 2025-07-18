from game import Obstruction
from board import Board

class UI:
    def __init__(self):
        self.board = Board()
        self.game = Obstruction(self.board, 3, 3)

    def place_player_obstruction(self):
        while True:
            try:
                row = int(input("Enter row: "))
                column = int(input("Enter column: "))
                break
            except ValueError:
                print("Invalid input")
        self.game.board.place_obstruction(row, column)
        self.game = Obstruction(self.board, row, column)

    def start(self):
        while True:
            print(self.game.board)
            self.place_player_obstruction()
            if self.game.board.placed == 49:
                print(self.game.board)
                print("Game Over! Computer wins!")
                break

ui = UI()
ui.start()