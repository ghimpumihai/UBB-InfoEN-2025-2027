from domain import Address
from repository import TextFileRepository
from services import Services
class UI:
    def __init__(self, service):
        self.service = service
    def add_address(self):
        try:
            address_id = int(input("Enter address ID: "))
            street_name = input("Enter street name: ")
            street_number = input("Enter street number: ")
            x=int(input("Enter x: "))
            y=int(input("Enter y: "))
            self.service.add_address(address_id,str(street_name),int(street_number),int(x),int(y))
        except Exception as e:
           print(e)

    def distance_from_d(self,d,x,y):
        list_address=self.service.distance_from_d(d,x,y)
        for i in sorted(list_address.keys()):
            print(list_address[i])

    def minimize_average(self):
        x,y=self.service.minimize_average()
        print(f"The x coordinate is {x} and the y coordinate is {y}")

    def menu(self):
        while True:
            print("1. Add address")
            print("2. What addresses at most distance d from a given point")
            print("3.Determine x,y coordinates for a new taxi station to minimize average distance")
            n=int(input("Enter your choice: "))
            if n==1:
                self.add_address()
            elif n==2:
                d=int(input("Enter the distance: "))
                x=int(input("Enter x: "))
                y=int(input("Enter y: "))
                self.distance_from_d(d,x,y)
            elif n==3:
                self.minimize_average()
            else:
                break


def initialize_repository(repository):
    initial_addresses = [
        Address(1, "theodor mihali", 10, 12, 20),
        Address(2, "theodor mihali", 15, 16, 30),
        Address(3, "mihail kogalniceanu", 1, 40, 45),
        Address(4, "dorobantilor", 20, 50, 100),
        Address(5, "dorobantilor", 22, 54, 100),
        Address(6, "salciilor", 2, 2, 20),
        Address(7, "salciilor", 50, 46, 18),
        Address(8, "mihai eminescu", 2, 90, 90),
        Address(9, "mihai eminescu", 3, 90, 92),
        Address(10, "titulescu", 10, 10, 12),
    ]
    if repository.get_all():
        return
    else:
        for address in initial_addresses:
            try:
                repository.add(address)
            except ValueError:
                pass
if __name__ == "__main__":
    repo = TextFileRepository('taxi.txt')
    initialize_repository(repo)
    service = Services(repo)
    ui = UI(service)
    ui.menu()