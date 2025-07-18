import configparser
from src.repository.repository import *
from src.services.services import *
from src.domain.person import *
from src.domain.activity import *
from faker import Faker
import random

class UIException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class UI:
    def __init__(self, service):
        self.service = service

    def display_persons(self):
        try:
            persons = self.service.list_persons()
            if not persons:
                print("No persons to display.")
            else:
                for person in persons:
                    print(person)
        except Exception as e:
            raise UIException(f"Error displaying persons: {e}")

    def display_activities(self):
        try:
            activities = self.service.list_activities()
            if not activities:
                print("No activities to display.")
            else:
                for activity in activities:
                    print(activity)
        except Exception as e:
            raise UIException(f"Error displaying activities: {e}")

    def display_search_persons_name(self, name):
        try:
            persons = self.service.search_persons_name(name)
            if not persons:
                print("No persons found.")
            else:
                for person in persons:
                    print(person)
        except Exception as e:
            raise UIException(f"Error searching persons by name: {e}")

    def display_search_persons_phone(self, phone_number):
        try:
            persons = self.service.search_persons_phone(phone_number)
            if not persons:
                print("No persons found.")
            else:
                for person in persons:
                    print(person)
        except Exception as e:
            raise UIException(f"Error searching persons by phone number: {e}")

    def display_search_activities_date_time(self, date, time):
        try:
            activities = self.service.search_activities_date_time(date, time)
            if not activities:
                print("No activities found.")
            else:
                for activity in activities:
                    print(activity)
        except Exception as e:
            raise UIException(f"Error searching activities by date and time: {e}")

    def display_search_activities_description(self, description):
        try:
            activities = self.service.search_activities_description(description)
            if not activities:
                print("No activities found.")
            else:
                for activity in activities:
                    print(activity)
        except Exception as e:
            raise UIException(f"Error searching activities by description: {e}")

    def add_person_ui(self):
        try:
            person_id = int(input("Enter person ID: "))
            name = input("Enter person name: ")
            phone_number = input("Enter phone number: ")
            self.service.add_person(person_id, name, phone_number)
            print("Person added successfully.")
        except Exception as e:
            raise UIException(f"Error adding person: {e}")

    def add_activity_ui(self):
        try:
            activity_id = int(input("Enter activity ID: "))
            number_persons = int(input("Enter the number of persons: "))
            person_id = ""
            for i in range(number_persons):
                if i != number_persons - 1:
                    person_id += input("Enter person ID: ") + ";"
                else:
                    person_id += input("Enter person ID: ")
            date = input("Enter date: ")
            time = input("Enter time: ")
            description = input("Enter description: ")
            self.service.add_activity(activity_id, person_id, date, time, description)
            print("Activity added successfully.")
        except Exception as e:
            raise UIException(f"Error adding activity: {e}")

    def print_activities_for_given_date(self,date):
        activities = self.service.activities_for_given_date(date)
        for activity in activities:
            print(activity)

    def print_busiest_days(self):
        days = self.service.busiest_days()
        for day in days:
            print(day)

    def print_activities_for_given_person(self,person_id):
        activities = self.service.activities_for_given_person(person_id)
        for activity in activities:
            print(activity)

    def menu_manage_persons_activities(self):
        print("1. Add person")
        print("2. Remove person")
        print("3. Update person")
        print("4. Add activity")
        print("5. Remove activity")
        print("6. Update activity")
        print("7. List persons")
        print("8. List activities")

    def big_menu(self):
        print("1. Manage persons and activities")
        print("2. Search for persons or activities")
        print("3. Statistics")
        print("4. Undo/Redo")

    def statistics_menu(self):
        print("1.Activities for a given date")
        print("2.Busiest days")
        print("3.Activities for a given person")

    def menu(self):
        while True:
            self.big_menu()
            while True:
                try:
                    choice = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("Invalid choice. Try again.")
            if choice == 1:
                self.menu_manage_persons_activities()
                while True:
                    try:
                        choice2 = int(input("Enter your choice: "))
                        break
                    except ValueError:
                        print("Invalid choice. Try again.")
                if choice2 == 1:
                    self.add_person_ui()
                elif choice2 == 2:
                    try:
                        person_id = int(input("Enter person ID: "))
                        self.service.remove_person(person_id)
                    except Exception as e:
                        raise UIException(f"Error removing person: {e}")
                elif choice2 == 3:
                    try:
                        person_id = int(input("Enter person ID: "))
                        name = input("Enter new person name: ")
                        phone_number = input("Enter new phone number: ")
                        self.service.update_person(person_id, name, phone_number)
                    except Exception as e:
                        raise UIException(f"Error updating person: {e}")
                elif choice2 == 4:
                    self.add_activity_ui()
                elif choice2 == 5:
                    try:
                        activity_id = int(input("Enter activity ID: "))
                        self.service.remove_activity(activity_id)
                    except Exception as e:
                        raise UIException(f"Error removing activity: {e}")
                elif choice2 == 6:
                    try:
                        activity_id = int(input("Enter activity ID: "))
                        number_persons = int(input("Enter the number of persons: "))
                        person_id = ""
                        for i in range(number_persons):
                            if i != number_persons - 1:
                                person_id += input("Enter person ID: ") + ";"
                            else:
                                person_id += input("Enter person ID: ")
                        date = input("Enter date: ")
                        time = input("Enter time: ")
                        description = input("Enter description: ")
                        self.service.update_activity(activity_id, person_id, date, time, description)
                    except Exception as e:
                        raise UIException(f"Error updating activity: {e}")
                elif choice2 == 7:
                    self.display_persons()
                elif choice2 == 8:
                    self.display_activities()
                else:
                    print("Invalid choice. Try again.")
            elif choice == 2:
                print("What do you want to search for?")
                print("1. Persons")
                print("2. Activities")
                while True:
                    try:
                        choice2 = int(input("Enter your choice: "))
                        break
                    except ValueError:
                        print("Invalid choice. Try again.")
                if choice2 == 1:
                    print("How do you want to search for persons?")
                    print("1. By name")
                    print("2. By phone number")
                    while True:
                        try:
                            choice3 = int(input("Enter your choice: "))
                            break
                        except ValueError:
                            print("Invalid choice. Try again.")
                    if choice3 == 1:
                        name = input("Enter the name: ")
                        self.display_search_persons_name(name)
                    elif choice3 == 2:
                        phone_number = input("Enter the phone number: ")
                        self.display_search_persons_phone(phone_number)
                elif choice2 == 2:
                    print("How do you want to search for activities?")
                    print("1. By date and time")
                    print("2. By description")
                    while True:
                        try:
                            choice3 = int(input("Enter your choice: "))
                            break
                        except ValueError:
                            print("Invalid choice. Try again.")
                    if choice3 == 1:
                        date = input("Enter the date: ")
                        time = input("Enter the time: ")
                        self.display_search_activities_date_time(date, time)
                    elif choice3 == 2:
                        description = input("Enter the description: ")
                        self.display_search_activities_description(description)
                else:
                    print("Invalid choice. Try again.")
            elif choice == 3:
                self.statistics_menu()
                while True:
                    try:
                        choice2 = int(input("Enter your choice: "))
                        break
                    except ValueError:
                        print("Invalid choice. Try again.")
                if choice2 == 1:
                    date = input("Enter the date: ")
                    self.print_activities_for_given_date(date)
                elif choice2 == 2:
                    self.print_busiest_days()
                elif choice2 == 3:
                    try:
                        person_id = int(input("Enter person ID: "))
                    except Exception as e:
                        raise UIException(f"Error displaying activities for given person: {e}")
                    self.print_activities_for_given_person(person_id)
            elif choice == 4:
                print("1.Undo")
                print("2.Redo")
                while True:
                    try:
                        choice2 = int(input("Enter your choice: "))
                        break
                    except ValueError:
                        print("Invalid choice. Try again.")
                if choice2 == 1:
                    try:
                        self.service.undo()
                    except Exception as e:
                        raise UIException(f"Error undoing: {e}")
                elif choice2 == 2:
                    try:
                        self.service.redo()
                    except Exception as e:
                        raise UIException(f"Error redoing: {e}")


def persons_add():
    persons=[]
    for _ in range(20):
        person_id = fake.unique.random_int(min=1, max=1000)
        name = fake.name()
        phone_number = fake.phone_number()
        persons.append(Person(person_id, name, phone_number))
    return persons
def activities_add(person_id_list):
    activities = []
    for _ in range(20):
        activity_id = fake.unique.random_int(min=1, max=1000)
        person_ids = [random.choice(person_id_list) for _ in range(fake.random_int(min=1, max=5))]
        res_person_ids = ';'.join(map(str, person_ids))
        date = fake.date()
        time = fake.time()
        description = fake.sentence()
        activity = Activity(activity_id, res_person_ids, date, time, description)
        activities.append(activity)
    return activities

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.properties')

    repository_type = config['REPOSITORY'].get('repository_type')
    person_memory = config['REPOSITORY'].get('person')
    activity_memory = config['REPOSITORY'].get('activity')
    fake = Faker()
    persons=persons_add()
    activities=activities_add(person_id_list=[person.get_person_id() for person in persons])
    if repository_type == 'memory':
        person_repo = MemoryRepositoryPerson()
        for i in persons:
            person_repo.add(i)
        activity_repo = MemoryRepositoryActivity()
        for i in activities:
            activity_repo.add(i)
    elif repository_type == 'text':
        person_repo = TextFileRepositoryPerson(person_memory)
        if not os.path.exists(person_memory):
            for i in persons:
                person_repo.add(i)
        activity_repo = TextFileRepositoryActivity(activity_memory)
        if not os.path.exists(activity_memory):
            for i in activities:
                activity_repo.add(i)
    elif repository_type == 'binary':
        person_repo = BinaryFileRepositoryPerson(person_memory)
        if not os.path.exists(person_memory):
            for i in persons:
                person_repo.add(i)
        activity_repo = BinaryFileRepositoryActivity(activity_memory)
        if not os.path.exists(activity_memory):
            for i in activities:
                activity_repo.add(i)
    service = Services(person_repo, activity_repo)
    ui = UI(service)
    ui.menu()