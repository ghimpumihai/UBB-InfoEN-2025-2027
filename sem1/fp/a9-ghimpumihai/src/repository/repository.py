import os
import pickle
from src.domain.person import Person
from src.domain.activity import Activity

class RepositoryException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class TextFileRepositoryPerson:
    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        self._persons = {}
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'r') as file:
            for line in file:
                person_id, name, phone_number = line.strip().split(',')
                person = Person(int(person_id), name, phone_number)
                self._persons[person.get_person_id()] = person

    def _save(self):
        with open(self.filename, 'w') as file:
            for person in self._persons.values():
                file.write(f"{person.get_person_id()},{person.get_name()},{person.get_phone_number()}\n")

    def add(self, person):
        """
        Add a new person to the repository.

        :param person: An instance of the Person class.
        :raises RepositoryException: If a person with the given ID already exists.
        """
        if person.get_person_id() in self._persons:
            raise RepositoryException("Person with this ID already exists.")
        self._persons[person.get_person_id()] = person
        self._save()

    def remove(self, person_id):
        """
        Remove a person from the repository.

        :param person_id: Unique identifier for the person to be removed.
        :raises RepositoryException: If no person with the given ID exists.
        """
        if person_id not in self._persons:
            raise RepositoryException("No person with this ID.")
        del self._persons[person_id]
        self._save()

    def update(self, person):
        """
        Update an existing person's details in the repository.

        :param person: An instance of the Person class with updated details.
        :raises RepositoryException: If no person with the given ID exists.
        """
        if person.get_person_id() not in self._persons:
            raise RepositoryException("No person with this ID.")
        self._persons[person.get_person_id()] = person
        self._save()

    def get_all(self):
        """
        List all persons in the repository.

        :return: A list of all persons.
        """
        return list(self._persons.values())

class TextFileRepositoryActivity:
    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        self._activities = {}
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'r') as file:
            for line in file:
                activity_id, person_ids, date, time, description = line.strip().split(',')
                activity = Activity(int(activity_id), person_ids, date, time, description)
                self._activities[activity.get_activity_id()] = activity

    def _save(self):
        with open(self.filename, 'w') as file:
            for activity in self._activities.values():
                person_ids = ''.join(activity.get_person_id())
                file.write(f"{activity.get_activity_id()},{person_ids},{activity.get_date()},{activity.get_time()},{activity.get_description()}\n")

    def add(self, activity):
        """
        Add a new activity to the repository.

        :param activity: An instance of the Activity class.
        :raises RepositoryException: If an activity with the given ID already exists.
        """
        if activity.get_activity_id() in self._activities:
            raise RepositoryException("Activity with this ID already exists.")
        self._activities[activity.get_activity_id()] = activity
        self._save()

    def remove(self, activity_id):
        """
        Remove an activity from the repository.

        :param activity_id: Unique identifier for the activity to be removed.
        :raises RepositoryException: If no activity with the given ID exists.
        """
        if activity_id not in self._activities:
            raise RepositoryException("No activity with this ID.")
        del self._activities[activity_id]
        self._save()

    def update(self, activity):
        """
        Update an existing activity's details in the repository.

        :param activity: An instance of the Activity class with updated details.
        :raises RepositoryException: If no activity with the given ID exists.
        """
        if activity.get_activity_id() not in self._activities:
            raise RepositoryException("No activity with this ID.")
        self._activities[activity.get_activity_id()] = activity
        self._save()

    def get_all(self):
        """
        List all activities in the repository.

        :return: A list of all activities.
        """
        return list(self._activities.values())

class MemoryRepositoryPerson:
    def __init__(self):
        self._persons = {}

    def add(self, person):
        """
        Add a new person to the repository.

        :param person: An instance of the Person class.
        :raises RepositoryException: If a person with the given ID already exists.
        """
        if person.get_person_id() in self._persons:
            raise RepositoryException("Person with this ID already exists.")
        self._persons[person.get_person_id()] = person

    def remove(self, person_id):
        """
        Remove a person from the repository.

        :param person_id: Unique identifier for the person to be removed.
        :raises RepositoryException: If no person with the given ID exists.
        """
        if person_id not in self._persons:
            raise RepositoryException("No person with this ID.")
        del self._persons[person_id]

    def update(self, person):
        """
        Update an existing person's details in the repository.

        :param person: An instance of the Person class with updated details.
        :raises RepositoryException: If no person with the given ID exists.
        """
        if person.get_person_id() not in self._persons:
            raise RepositoryException("No person with this ID.")
        self._persons[person.get_person_id()] = person

    def get_all(self):
        """
        List all persons in the repository.

        :return: A list of all persons.
        """
        return list(self._persons.values())

class MemoryRepositoryActivity:
    def __init__(self):
        self._activities = {}

    def add(self, activity):
        """
        Add a new activity to the repository.

        :param activity: An instance of the Activity class.
        :raises RepositoryException: If an activity with the given ID already exists.
        """
        if activity.get_activity_id() in self._activities:
            raise RepositoryException("Activity with this ID already exists.")
        self._activities[activity.get_activity_id()] = activity

    def remove(self, activity_id):
        """
        Remove an activity from the repository.

        :param activity_id: Unique identifier for the activity to be removed.
        :raises RepositoryException: If no activity with the given ID exists.
        """
        if activity_id not in self._activities:
            raise RepositoryException("No activity with this ID.")
        del self._activities[activity_id]

    def update(self, activity):
        """
        Update an existing activity's details in the repository.

        :param activity: An instance of the Activity class with updated details.
        :raises RepositoryException: If no activity with the given ID exists.
        """
        if activity.get_activity_id() not in self._activities:
            raise RepositoryException("No activity with this ID.")
        self._activities[activity.get_activity_id()] = activity

    def get_all(self):
        """
        List all activities in the repository.

        :return: A list of all activities.
        """
        return list(self._activities.values())


class BinaryFileRepositoryPerson:
    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                self._persons = pickle.load(file)
        else:
            self._persons = {}

    def _save(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self._persons, file)

    def add(self, person):
        """
        Add a new person to the repository.

        :param person: An instance of the Person class.
        :raises RepositoryException: If a person with the given ID already exists.
        """
        if person.get_person_id() in self._persons:
            raise RepositoryException("Person with this ID already exists.")
        self._persons[person.get_person_id()] = person
        self._save()

    def remove(self, person_id):
        """
        Remove a person from the repository.

        :param person_id: Unique identifier for the person to be removed.
        :raises RepositoryException: If no person with the given ID exists.
        """
        if person_id not in self._persons:
            raise RepositoryException("No person with this ID.")
        del self._persons[person_id]
        self._save()

    def update(self, person):
        """
        Update an existing person's details in the repository.

        :param person: An instance of the Person class with updated details.
        :raises RepositoryException: If no person with the given ID exists.
        """
        if person.get_person_id() not in self._persons:
            raise RepositoryException("No person with this ID.")
        self._persons[person.get_person_id()] = person
        self._save()

    def get_all(self):
        """
        List all persons in the repository.

        :return: A list of all persons.
        """
        return list(self._persons.values())

class BinaryFileRepositoryActivity:
    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                self._activities = pickle.load(file)
        else:
            self._activities = {}

    def _save(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self._activities, file)

    def add(self, activity):
        """
        Add a new activity to the repository.

        :param activity: An instance of the Activity class.
        :raises RepositoryException: If an activity with the given ID already exists.
        """
        if activity.get_activity_id() in self._activities:
            raise RepositoryException("Activity with this ID already exists.")
        self._activities[activity.get_activity_id()] = activity
        self._save()

    def remove(self, activity_id):
        """
        Remove an activity from the repository.

        :param activity_id: Unique identifier for the activity to be removed.
        :raises RepositoryException: If no activity with the given ID exists.
        """
        if activity_id not in self._activities:
            raise RepositoryException("No activity with this ID.")
        del self._activities[activity_id]
        self._save()

    def update(self, activity):
        """
        Update an existing activity's details in the repository.

        :param activity: An instance of the Activity class with updated details.
        :raises RepositoryException: If no activity with the given ID exists.
        """
        if activity.get_activity_id() not in self._activities:
            raise RepositoryException("No activity with this ID.")
        self._activities[activity.get_activity_id()] = activity
        self._save()

    def get_all(self):
        """
        List all activities in the repository.

        :return: A list of all activities.
        """
        return list(self._activities.values())