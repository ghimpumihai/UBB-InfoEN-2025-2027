# tests/test_repository.py
import unittest
from src.repository.repository import MemoryRepositoryPerson, MemoryRepositoryActivity, RepositoryException
from src.domain.person import Person
from src.domain.activity import Activity

class TestMemoryRepositoryPerson(unittest.TestCase):
    def setUp(self):
        self.repo = MemoryRepositoryPerson()

    def test_add_person(self):
        person = Person(1, "John Doe", "1234567890")
        self.repo.add(person)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.get_all()[0].get_name(), "John Doe")

    def test_add_person_duplicate_id(self):
        person1 = Person(1, "John Doe", "1234567890")
        person2 = Person(1, "Jane Doe", "0987654321")
        self.repo.add(person1)
        with self.assertRaises(RepositoryException):
            self.repo.add(person2)

    def test_update_person(self):
        person = Person(1, "John Doe", "1234567890")
        self.repo.add(person)
        updated_person = Person(1, "Jane Doe", "0987654321")
        self.repo.update(updated_person)
        self.assertEqual(self.repo.get_all()[0].get_name(), "Jane Doe")

    def test_remove_person(self):
        person = Person(1, "John Doe", "1234567890")
        self.repo.add(person)
        self.repo.remove(1)
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_get_all_persons(self):
        person1 = Person(1, "John Doe", "1234567890")
        person2 = Person(2, "Jane Doe", "0987654321")
        self.repo.add(person1)
        self.repo.add(person2)
        self.assertEqual(len(self.repo.get_all()), 2)

class TestMemoryRepositoryActivity(unittest.TestCase):
    def setUp(self):
        self.repo = MemoryRepositoryActivity()

    def test_add_activity(self):
        activity = Activity(1, "1;2", "2023-10-10", "10:00", "Meeting")
        self.repo.add(activity)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.get_all()[0].get_description(), "Meeting")

    def test_add_activity_duplicate_id(self):
        activity1 = Activity(1, "1;2", "2023-10-10", "10:00", "Meeting")
        activity2 = Activity(1, "3;4", "2023-10-11", "11:00", "Workshop")
        self.repo.add(activity1)
        with self.assertRaises(RepositoryException):
            self.repo.add(activity2)

    def test_update_activity(self):
        activity = Activity(1, "1;2", "2023-10-10", "10:00", "Meeting")
        self.repo.add(activity)
        updated_activity = Activity(1, "3;4", "2023-10-11", "11:00", "Workshop")
        self.repo.update(updated_activity)
        self.assertEqual(self.repo.get_all()[0].get_description(), "Workshop")

    def test_remove_activity(self):
        activity = Activity(1, "1;2", "2023-10-10", "10:00", "Meeting")
        self.repo.add(activity)
        self.repo.remove(1)
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_get_all_activities(self):
        activity1 = Activity(1, "1;2", "2023-10-10", "10:00", "Meeting")
        activity2 = Activity(2, "3;4", "2023-10-11", "11:00", "Workshop")
        self.repo.add(activity1)
        self.repo.add(activity2)
        self.assertEqual(len(self.repo.get_all()), 2)

if __name__ == '__main__':
    unittest.main()