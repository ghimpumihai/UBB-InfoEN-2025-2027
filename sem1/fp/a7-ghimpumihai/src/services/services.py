import os
from src.domain.domain import Student
from src.repository.repository import TextFileRepository, BinaryFileRepository, MemoryRepository

class Test:
    def __init__(self, repository):
        self.repository = repository

    def add_student_test(self):
        student = Student(1, "Alice", 101)
        self.repository.add(student)
        assert self.repository.get_all() == [student]
        student = Student(2, "Bob", 101)
        self.repository.add(student)
        assert len(self.repository.get_all()) == 2

class Service:
    def __init__(self, repository):
        self.repository = repository
        self.undo_stack = []

    def add_student(self, student_id, name, group):
        """
        Add a student to the repository.
        :param student_id: The id of the student.
        :param name: Name of the student.
        :param group: Group of the student.
        :return: None
        """
        student = Student(student_id, name, group)
        self.undo_stack.append(("remove", student_id))
        self.repository.add(student)
    def remove_students_by_group(self, group):
        all_students = self.repository.get_all()
        removed_students = [s for s in all_students if s.group == group]
        self.undo_stack.append(("add", removed_students))
        for student in removed_students:
            self.repository.remove(student.student_id)

    def undo(self):
        if not self.undo_stack:
            raise ValueError("Nothing to undo.")
        action, data = self.undo_stack.pop()
        if action == "remove":
            self.repository.remove(data)
        elif action == "add":
            for student in data:
                self.repository.add(student)

    def list_students(self):
        return self.repository.get_all()

test = Test(MemoryRepository())
test.add_student_test()
test2 = Test(TextFileRepository("test_students.txt"))
test2.add_student_test()
test3 = Test(BinaryFileRepository("test_students.bin"))
test3.add_student_test()
os.remove("test_students.txt")
os.remove("test_students.bin")