# tests/test_services.py
import unittest

from src.repository.repository import MemoryRepositoryPerson, MemoryRepositoryActivity, RepositoryException
from src.services.services import Services

class TestServices(unittest.TestCase):
    def setUp(self):
        self.person_repo = MemoryRepositoryPerson()
        self.activity_repo = MemoryRepositoryActivity()
        self.service = Services(self.person_repo, self.activity_repo)

    def test_add_person(self):
        self.service.add_person(1, "John Doe", "1234567890")
        persons = self.service.list_persons()
        self.assertEqual(len(persons), 1)
        self.assertEqual(persons[0].get_name(), "John Doe")

    def test_add_person_duplicate_id(self):
        self.service.add_person(1, "John Doe", "1234567890")
        with self.assertRaises(RepositoryException):
            self.service.add_person(1, "Jane Doe", "0987654321")

    def test_update_person(self):
        self.service.add_person(1, "John Doe", "1234567890")
        self.service.update_person(1, "Jane Doe", "0987654321")
        persons = self.service.list_persons()
        self.assertEqual(persons[0].get_name(), "Jane Doe")
        self.assertEqual(persons[0].get_phone_number(), "0987654321")

    def test_remove_person(self):
        self.service.add_person(1, "John Doe", "1234567890")
        self.service.remove_person(1)
        persons = self.service.list_persons()
        self.assertEqual(len(persons), 0)

    def test_list_persons(self):
        self.service.add_person(1, "John Doe", "1234567890")
        self.service.add_person(2, "Jane Doe", "0987654321")
        persons = self.service.list_persons()
        self.assertEqual(len(persons), 2)

    def test_add_activity(self):
        self.service.add_activity(1, [1, 2], "2023-10-10", "10:00", "Meeting")
        activities = self.service.list_activities()
        self.assertEqual(len(activities), 1)
        self.assertEqual(activities[0].get_description(), "Meeting")

    def test_add_activity_duplicate_id(self):
        self.service.add_activity(1, [1, 2], "2023-10-10", "10:00", "Meeting")
        with self.assertRaises(RepositoryException):
            self.service.add_activity(1, [3, 4], "2023-10-11", "11:00", "Workshop")

    def test_update_activity(self):
        self.service.add_activity(1, [1, 2], "2023-10-10", "10:00", "Meeting")
        self.service.update_activity(1, [3, 4], "2023-10-11", "11:00", "Workshop")
        activities = self.service.list_activities()
        self.assertEqual(activities[0].get_description(), "Workshop")
        self.assertEqual(activities[0].get_date(), "2023-10-11")

    def test_remove_activity(self):
        self.service.add_activity(1, [1, 2], "2023-10-10", "10:00", "Meeting")
        self.service.remove_activity(1)
        activities = self.service.list_activities()
        self.assertEqual(len(activities), 0)

    def test_list_activities(self):
        self.service.add_activity(1, [1, 2], "2023-10-10", "10:00", "Meeting")
        self.service.add_activity(2, [3, 4], "2023-10-11", "11:00", "Workshop")
        activities = self.service.list_activities()
        self.assertEqual(len(activities), 2)
