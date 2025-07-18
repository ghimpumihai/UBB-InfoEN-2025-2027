# src/services/services.py
from src.domain.person import Person
from src.domain.activity import Activity
from src.services.undo_service import FunctionCall, Operation, CascadingOperation, UndoService

class Services:
    def __init__(self, repository_person, repository_activity):
        self.repository_person = repository_person
        self.repository_activity = repository_activity
        self.undo_service = UndoService()

    def add_person(self, person_id, name, phone_number):
        person = Person(person_id, name, phone_number)
        self.repository_person.add(person)
        undo = FunctionCall(self.repository_person.remove, person_id)
        redo = FunctionCall(self.repository_person.add, person)
        operation = Operation(undo, redo)
        self.undo_service.record(operation)

    def update_person(self, person_id, name, phone_number):
        old_person = self.repository_person._persons[person_id]
        new_person = Person(person_id, name, phone_number)
        self.repository_person.update(new_person)
        undo = FunctionCall(self.repository_person.update, old_person)
        redo = FunctionCall(self.repository_person.update, new_person)
        operation = Operation(undo, redo)
        self.undo_service.record(operation)

    def remove_person(self, person_id):
        person = self.repository_person._persons[person_id]
        activities = [activity for activity in self.repository_activity._activities.values() if str(person_id) in activity.get_person_id().split(';')]
        cascading_operation = CascadingOperation()

        # Remove person
        self.repository_person.remove(person_id)
        undo_person = FunctionCall(self.repository_person.add, person)
        redo_person = FunctionCall(self.repository_person.remove, person_id)
        operation_person = Operation(undo_person, redo_person)
        cascading_operation.add_operation(operation_person)

        # Remove related activities
        for activity in activities:
            self.repository_activity.remove(activity.get_activity_id())
            undo_activity = FunctionCall(self.repository_activity.add, activity)
            redo_activity = FunctionCall(self.repository_activity.remove, activity.get_activity_id())
            operation_activity = Operation(undo_activity, redo_activity)
            cascading_operation.add_operation(operation_activity)

        self.undo_service.record(cascading_operation)

    def add_activity(self, activity_id, person_id, date, time, description):
        activity = Activity(activity_id, person_id, date, time, description)
        self.repository_activity.add(activity)
        undo = FunctionCall(self.repository_activity.remove, activity_id)
        redo = FunctionCall(self.repository_activity.add, activity)
        operation = Operation(undo, redo)
        self.undo_service.record(operation)

    def update_activity(self, activity_id, person_id, date, time, description):
        old_activity = self.repository_activity._activities[activity_id]
        new_activity = Activity(activity_id, person_id, date, time, description)
        self.repository_activity.update(new_activity)
        undo = FunctionCall(self.repository_activity.update, old_activity)
        redo = FunctionCall(self.repository_activity.update, new_activity)
        operation = Operation(undo, redo)
        self.undo_service.record(operation)

    def remove_activity(self, activity_id):
        activity = self.repository_activity._activities[activity_id]
        self.repository_activity.remove(activity_id)
        undo = FunctionCall(self.repository_activity.add, activity)
        redo = FunctionCall(self.repository_activity.remove, activity_id)
        operation = Operation(undo, redo)
        self.undo_service.record(operation)

    def undo(self):
        self.undo_service.undo()

    def redo(self):
        self.undo_service.redo()

    def list_persons(self):
        """
        List all persons in the repository.

        :return: A list of all persons.
        """
        return self.repository_person.get_all()

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

    def activities_for_given_date(self, date):
        return [activity for activity in self.repository_activity.get_all() if activity.get_date() == date]

    def busiest_days(self):
        days = {}
        for activity in self.repository_activity.get_all():
            if activity.get_date() in days:
                days[activity.get_date()] += 1
            else:
                days[activity.get_date()] = 1
        return [key for key, value in days.items() if value == max(days.values())]

    def activities_for_given_person(self, person_id):
        activities = self.repository_activity.get_all()
        result = []
        for i in activities:
            str_person_id = i.get_person_id()
            activity_person_id = str_person_id.split(";")
            for j in activity_person_id:
                if str(j) == str(person_id):
                    result.append(i)
        return result