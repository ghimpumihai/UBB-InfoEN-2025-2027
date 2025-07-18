from src.domain.person import Person
from src.domain.activity import Activity

class Services:
    def __init__(self, repository_person, repository_activity):
        """
        Initialize the Services class with person and activity repositories.

        :param repository_person: Repository for managing persons.
        :param repository_activity: Repository for managing activities.
        """
        self.repository_person = repository_person
        self.repository_activity = repository_activity

    def add_person(self, person_id, name, phone_number):
        """
        Add a new person to the repository.

        :param person_id: Unique identifier for the person.
        :param name: Name of the person.
        :param phone_number: Phone number of the person.
        :raises RepositoryException: If a person with the given ID already exists.
        """
        person = Person(person_id, name, phone_number)
        self.repository_person.add(person)

    def update_person(self, person_id, name, phone_number):
        """
        Update an existing person's details in the repository.

        :param person_id: Unique identifier for the person.
        :param name: New name of the person.
        :param phone_number: New phone number of the person.
        :raises RepositoryException: If no person with the given ID exists.
        """
        for person in self.repository_person.get_all():
            if person.get_person_id() == person_id:
                person.set_name(name)
                person.set_phone_number(phone_number)
        person=Person(person_id, name, phone_number)
        self.repository_person.update(person)

    def remove_person(self, person_id):
        """
        Remove a person from the repository.

        :param person_id: Unique identifier for the person to be removed.
        :raises RepositoryException: If no person with the given ID exists.
        """
        self.repository_person.remove(person_id)

    def list_persons(self):
        """
        List all persons in the repository.

        :return: A list of all persons.
        """
        return self.repository_person.get_all()

    def add_activity(self, activity_id, person_id, date, time, description):
        """
        Add a new activity to the repository.

        :param activity_id: Unique identifier for the activity.
        :param person_id: List of person IDs associated with the activity.
        :param date: Date of the activity.
        :param time: Time of the activity.
        :param description: Description of the activity.
        :raises RepositoryException: If an activity with the given ID already exists.
        """
        activity = Activity(activity_id, person_id, date, time, description)
        self.repository_activity.add(activity)

    def update_activity(self, activity_id, person_id, date, time, description):
        """
        Update an existing activity's details in the repository.

        :param activity_id: Unique identifier for the activity.
        :param person_id: List of new person IDs associated with the activity.
        :param date: New date of the activity.
        :param time: New time of the activity.
        :param description: New description of the activity.
        :raises RepositoryException: If no activity with the given ID exists.
        """
        for activity in self.repository_activity.get_all():
            if activity.get_activity_id() == activity_id:
                activity.set_person_id(person_id)
                activity.set_date(date)
                activity.set_time(time)
                activity.set_description(description)
        activity=Activity(activity_id, person_id, date, time, description)
        self.repository_activity.update(activity)

    def remove_activity(self, activity_id):
        """
        Remove an activity from the repository.

        :param activity_id: Unique identifier for the activity to be removed.
        :raises RepositoryException: If no activity with the given ID exists.
        """
        self.repository_activity.remove(activity_id)

    def list_activities(self):
        """
        List all activities in the repository.

        :return: A list of all activities.
        """
        return self.repository_activity.get_all()

    def search_persons_name(self, name):
        return [person for person in self.repository_person.get_all() if name.lower() in person.get_name().lower()]

    def search_persons_phone(self, phone_number):
        return [person for person in self.repository_person.get_all() if phone_number in person.get_phone_number()]

    def search_activities_date_time(self, date, time):
        return [activity for activity in self.repository_activity.get_all() if activity.get_date() == date and activity.get_time() == time]

    def search_activities_description(self, description):
        return [activity for activity in self.repository_activity.get_all() if description.lower() in activity.get_description().lower()]