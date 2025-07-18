import random


class Service:
    def __init__(self,board,repository):
        self.board=board
        self.repository=repository

    def check_place(self,x,y,value):
        if x<0 or y<0 or x>=self.board.size or y>=self.board.size:
            raise IndexError("Indexes have to be inside the board")
        if self.board.board[x][y]!=0:
            raise ValueError("Place already taken")
        if value!=1 and value!=2:
            raise ValueError("Invalid value")
        return True

    def is_won(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                nr=0
                for k in range(self.board.size):
                    if j+k<self.board.size and self.board.board[i][j+k]!=0:
                        if self.board.board[i][j+k]==self.board.board[i][j]:
                            nr+=1
                        else:
                            nr=0
                    else:
                        nr=0
                    if nr==self.board.win:
                        return True
        for i in range(self.board.size):
            for j in range(self.board.size):
                nr = 0
                for k in range(self.board.size):
                    if i+k<self.board.size and self.board.board[i+k][j]!=0:
                        if self.board.board[i][j]==self.board.board[i+k][j]:
                            nr+=1
                        else:
                            nr=0
                    else:
                        nr=0
                    if nr==self.board.win:
                       return True
        for i in range(self.board.size):
            for j in range(self.board.size):
                nr = 0
                for k in range(self.board.size):
                    if i+k<self.board.size and j+k<self.board.size and self.board.board[i+k][j+k]!=0:
                        if self.board.board[i+k][j+k]==self.board.board[i][j]:
                            nr+=1
                        else:
                            nr=0
                    else:
                        nr=0
                    if nr==self.board.win:
                        return True


        for i in range(self.board.size):
            for j in range(self.board.size):
                nr = 0
                for k in range(self.board.size):
                    if i+k<self.board.size and j-k>0 and self.board.board[i+k][j-k]!=0:
                        if self.board.board[i+k][j-k]==self.board.board[i][j]:
                            nr+=1
                        else:
                            nr=0
                    else:
                        nr=0
                    if nr==self.board.win:
                        return True

        return False

    def next_move_won(self):
        for i in range(self.board.size):
            for j in range(self.board.size):
                nr = 0
                for k in range(self.board.size):
                    if j + k < self.board.size and self.board.board[i][j+k] != 0:
                        if self.board.board[i][j + k] == self.board.board[i][j]:
                            nr += 1
                        else:
                            nr = 0
                    else:
                        nr = 0
                    if nr == self.board.win - 1:
                        if j + self.board.win-1 < self.board.size and self.board.board[i][j + self.board.win-1] == 0:
                            return i, j + self.board.win-1
                        elif j - 1 > 0 and self.board.board[i][j - 1] == 0:
                            return i, j - 1
        for i in range(self.board.size):
            for j in range(self.board.size):
                nr = 0
                for k in range(self.board.size):
                    if i + k < self.board.size and self.board.board[i + k][j] != 0:
                        if self.board.board[i][j] == self.board.board[i + k][j]:
                            nr += 1
                        else:
                            nr = 0
                    else:
                        nr = 0
                    if nr == self.board.win - 1:
                        if i + self.board.win-1 < self.board.size and self.board.board[i + self.board.win-1][j] == 0:
                            return i + self.board.win-1, j
                        elif i > 0 and self.board.board[i - 1][j] == 0:
                            return i - 1, j
        for i in range(self.board.size):
            for j in range(self.board.size):
                nr = 0
                for k in range(self.board.size):
                    if i + k < self.board.size and j + k < self.board.size and self.board.board[i + k][j + k] != 0:
                        if self.board.board[i + k][j + k] == self.board.board[i][j]:
                            nr += 1
                        else:
                            nr = 0
                    else:
                        nr = 0
                    if nr == self.board.win - 1:
                        if i + self.board.win-1 < self.board.size and j + self.board.win-1 < self.board.size and self.board.board[i+self.board.win-1][j + self.board.win-1] == 0:
                            return i + 4, j + 4
                        elif i - 1 > 0 and j - 1 > 0 and self.board.board[i-1][j - 1] == 0:
                            return i - 1, j - 1

        for i in range(self.board.size):
            for j in range(self.board.size):
                nr = 0
                for k in range(self.board.size):
                    if i + k < self.board.size and j - k > 0 and self.board.board[i + k][j - k] != 0:
                        if self.board.board[i + k][j - k] == self.board.board[i][j]:
                            nr += 1
                        else:
                            nr = 0
                    else:
                        nr = 0
                    if nr == self.board.win - 1:
                        if i + self.board.win-1 < self.board.size and j - self.board.win-1 > 0 and self.board.board[i + self.board.win-1][j - self.board.win-1] == 0:
                            return i + self.board.win-1, j - self.board.win-1
                        elif i - 1 > 0 and j + 1 < self.board.size and self.board.board[i][j - 1] == 0:
                            return i - 1, j + 1
        return False

    def place(self,x,y,value):
        self.board.board[x][y]=value
        if self.next_move_won():
            x=self.next_move_won()[0]
            y=self.next_move_won()[1]
            self.board.board[x][y]=3-value
        else:
            x=random.randint(0,self.board.size-1)
            y=random.randint(0,self.board.size-1)
            while self.board.board[x][y]!=0:
                x=random.randint(0,self.board.size-1)
                y=random.randint(0,self.board.size-1)
            self.board.board[x][y]=3-value


    def is_full(self):
        for i in self.board.board:
            for j in i:
                if j==0:
                    return False
        return True