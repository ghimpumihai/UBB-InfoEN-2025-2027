import texttable as t
from board import Board
from service import Service
from src.repository import Repository
class UI:
    def __init__(self,service):
        self.service=service
    def menu(self):
        print("1.New game")
        print("2.Load game")

    def new_game(self):
        while True:
            try:
                size=int(input("Enter size: "))
                win=int(input("Enter win: "))
                break
            except ValueError as ve:
                print(ve)
        filename=input("Enter filename:")
        self.service=Service(Board(size,win),Repository(filename))

    def load_game(self):
        filename=input("Enter filename:")
        repository=Repository(filename)
        self.service=Service(repository.get_board(),repository)

    def run(self):
        #self.menu()
        # while True:
        #     try:
        #         option=int(input("Enter option: "))
        #         if option==1:
        #             self.new_game()
        #             break
        #         elif option==2:
        #             self.load_game()
        #             break
        #     except ValueError as ve:
        #         print(ve)

        table=t.Texttable()
        row=[" "]*self.service.board.size
        for i in range(self.service.board.size):
            table.add_row(row)
        print(table.draw())
        while True:
            while True:
                try:
                    x=int(input("Enter x: "))
                    y=int(input("Enter y: "))
                    value=int(input("Enter value: "))
                    self.service.check_place(x,y,value)
                    break
                except Exception as ve:
                    print(ve)
            try:
                self.service.place(x, y, value)
            except:
                print("Invalid move")
            table = t.Texttable()
            for i in self.service.board.board:
                row=[]
                for j in i:
                    if j==0:
                        row.append(" ")
                    elif j==1:
                        row.append("X")
                    elif j==2:
                        row.append("O")
                table.add_row(row)
            print(table.draw())
            # print("Do you want to save the game?")
            # print("1.Yes")
            # print("2.No")
            # try:
            #     option=int(input("Enter option: "))
            # except ValueError as ve:
            #     print(ve)

            # if option==1:
            #     self.service.repository.save(self.service.board)
            #     print("Game saved")
            if self.service.is_won():
                print("You won!")
                break
            else:
                if self.service.is_full():
                    print("Computer wins!")
                    break

if __name__=="__main__":
    service=Service(Board(3,3),Repository("no.txt"))
    ui=UI(service)
    ui.run()
