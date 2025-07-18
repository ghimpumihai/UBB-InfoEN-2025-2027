from src.domain.domain import Student
from src.repository.repository import TextFileRepository, BinaryFileRepository, MemoryRepository
from src.services.services import Service
class UI:
    def __init__(self, service):
        self.service = service

    def menu(self):
        while True:
            print("Menu:")
            print("1. Add student")
            print("2. Display students")
            print("3. Filter students by group")
            print("4. Undo")
            print("5. Exit")
            while True:
                try:
                    choice = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("Invalid choice. Try again.")
            try:
                if choice == 1:
                    self.add_student()
                elif choice == 2:
                    self.display_students()
                elif choice == 3:
                    self.remove_students_by_group()
                elif choice == 4:
                    self.service.undo()
                elif choice == 5:
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError as ve:
                print(ve)

    def add_student(self):
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        group = int(input("Enter group: "))
        self.service.add_student(student_id, name, group)

    def display_students(self):
        students = self.service.list_students()
        if not students:
            print("No students to display.")
        else:
            for student in students:
                print(student)

    def remove_students_by_group(self):
        group = int(input("Enter group to remove: "))
        self.service.remove_students_by_group(group)
def initialize_repository(repository):
    if repository.get_all():
        return

    initial_students = [
        Student(1, "Alice", 101),
        Student(2, "Bob", 102),
        Student(3, "Charlie", 103),
        Student(4, "David", 101),
        Student(5, "Eve", 102),
        Student(6, "Frank", 103),
        Student(7, "Grace", 101),
        Student(8, "Hannah", 102),
        Student(9, "Ivy", 103),
        Student(10, "Jack", 104),
    ]
    for student in initial_students:
        try:
            repository.add(student)
        except ValueError:
            pass
if __name__ == "__main__":
    repo = TextFileRepository('students.txt') # Or BinaryFileRepository('students.bin') or MemoryRepository() or TextFileRepository('students.txt')
    initialize_repository(repo)
    service = Service(repo)
    ui = UI(service)
    ui.menu()