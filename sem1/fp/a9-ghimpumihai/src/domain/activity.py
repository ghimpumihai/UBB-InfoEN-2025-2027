class Activity:
    def __init__(self, activity_id, person_id: str, date, time, description):
        self.__activity_id = activity_id
        self.__person_id = person_id
        self.__date = date
        self.__time = time
        self.__description = description

    def get_activity_id(self):
        return self.__activity_id

    def get_person_id(self):
        return self.__person_id

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_description(self):
        return self.__description

    def set_person_id(self, new_person_id):
        self.__person_id = new_person_id

    def set_date(self, new_date):
        self.__date = new_date

    def set_time(self, new_time):
        self.__time = new_time

    def set_description(self, new_description):
        self.__description = new_description

    def __str__(self):
        return f"Activity ID: {self.__activity_id}, Persons: {self.__person_id}, Date: {self.__date}, Time: {self.__time}, Description: {self.__description}"