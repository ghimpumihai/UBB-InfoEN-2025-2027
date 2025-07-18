class Student:
    def __init__(self, student_id, name, group):
        self.student_id = student_id
        self.name = name
        self.group = group

    def __str__(self):
        return f"Student(id={self.student_id}, name='{self.name}', group={self.group})"
