class Board:
    def __init__(self,size,win):
        self.size=size
        self.win=win
        self.board=[[0 for i in range(size)] for j in range(size)]
    def __iter__(self):
        return iter(self.board)
