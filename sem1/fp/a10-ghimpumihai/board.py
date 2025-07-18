from texttable import Texttable

class ObstructionBoard:
    def __init__(self):
        self.obstruction_board = [[0] * 7 for _ in range(7)]
        self.placed=0
        self.turn=1

    def check_placement(self,row:int,column:int):
        if row < 0 or row > 6 or column < 0 or column > 6:
            return False
        if self.obstruction_board[row][column] != 0:
            return False
        return True

    def place_obstruction(self,row:int,column:int):
        if self.check_placement(row,column):
            if self.turn == 1:
                self.placed+=1
                self.obstruction_board[row][column] = 1
                self.block_cells(row, column)
                self.turn = 2
            else:
                self.placed+=1
                self.obstruction_board[row][column] = 2
                self.block_cells(row, column)
                self.turn = 1
        else:
            if self.turn==2:
                print("Invalid placement")

    def block_cells(self,row,column):
       for i in range(-1,2):
           for j in range(-1,2):
               if 0 <= row + i <= 6 and 0 <= column + j <= 6:
                   if self.obstruction_board[row+i][column+j] == 0:
                        self.obstruction_board[row+i][column+j] = -1
                        self.placed+=1
       self.obstruction_board[row][column] = self.turn

class Board(ObstructionBoard):
    def __init__(self):
        super().__init__()
    def __str__(self):
        t=Texttable()
        for row in range(7):
            row_data = [' '] * 7
            for column in range(7):
                symbol = ' '
                if self.obstruction_board[row][column] == 1:
                    symbol = 'O'
                elif self.obstruction_board[row][column] == 2:
                    symbol= 'X'
                elif self.obstruction_board[row][column] == -1:
                    symbol = 'b'
                row_data[column] = symbol
            t.add_row(row_data)
        return t.draw()

