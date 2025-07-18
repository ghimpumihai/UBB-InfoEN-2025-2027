import os
class Repository:
    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        self.board = []
        self.size=0
        self.win=0
        if not os.path.exists(self.filename):
            return
        nr=0
        with open(self.filename, 'r') as file:
            for line in file:
                if nr==0:
                    self.size=int(line)
                elif nr==1:
                    self.win=int(line)
                else:
                    self.board.append(line)

    def save(self, board):
        with open(self.filename, 'w') as file:
            file.write(str(self.size)+'\n')
            file.write(str(self.win)+'\n')
            for i in board:
                for j in board[i]:
                    file.write(str(j)+' ')

    def get_board(self):
        return self.board
