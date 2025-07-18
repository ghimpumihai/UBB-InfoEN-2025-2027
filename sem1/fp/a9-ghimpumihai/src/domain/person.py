# src/domain/person.py
class Person:
    def __init__(self, person_id, name, phone_number):
        self.__person_id = person_id
        self.__name = name
        self.__phone_number = phone_number

    def get_person_id(self):
        return self.__person_id

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def set_name(self, new_name):
        self.__name = new_name

    def set_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

    def __str__(self):
        return f"Person ID: {self.__person_id}, Name: {self.__name}, Phone Number: {self.__phone_number}"