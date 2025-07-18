import os
import pickle
from src.domain.domain import Student
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

class TextFileRepository:
    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        self.students = {}
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'r') as file:
            for line in file:
                student_id, name, group = line.strip().split(',')
                self.students[int(student_id)] = Student(int(student_id), name, int(group))
    def _save(self):
        with open(self.filename, 'w') as file:
            for student in self.students.values():
                file.write(f"{student.student_id},{student.name},{student.group}\n")

    def add(self, student):
        """
        Add a student to the repository.
        :param student: The student that will be added to the repository.
        :return: None
        """
        if student.student_id in self.students:
            raise ValueError("Student with this ID already exists.")
        self.students[student.student_id] = student
        self._save()

    def remove(self, student_id):
        if student_id not in self.students:
            raise ValueError("No student with this ID.")
        del self.students[student_id]
        self._save()

    def get_all(self):
        return list(self.students.values())

class MemoryRepository:
    def __init__(self):
        self.students = {}

    def add(self, student):
        """
        Add a student to the repository.
        :param student: The student that will be added to the repository.
        :return: None
        """
        if student.student_id in self.students:
            raise ValueError("Student with this ID already exists.")
        self.students[student.student_id] = student

    def remove(self, student_id):
        if student_id not in self.students:
            raise ValueError("No student with this ID.")
        del self.students[student_id]

    def get_all(self):
        return list(self.students.values())

class BinaryFileRepository:
    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                self.students = pickle.load(file)
        else:
            self.students = {}

    def _save(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.students, file)

    def add(self, student):
        """
        The function adds a student to the repository.
        :param student: The student that will be added to the repository.
        :return: None
        """
        if student.student_id in self.students:
            raise ValueError("Student with this ID already exists.")
        self.students[student.student_id] = student
        self._save()

    def remove(self, student_id):
        if student_id not in self.students:
            raise ValueError("No student with this ID.")
        del self.students[student_id]
        self._save()

    def get_all(self):
        return list(self.students.values())

test=Test(MemoryRepository())
test.add_student_test()
test2=Test(TextFileRepository("test_students.txt"))
test2.add_student_test()
test3=Test(BinaryFileRepository("test_students.bin"))
test3.add_student_test()
os.remove("test_students.txt")
os.remove("test_students.bin")