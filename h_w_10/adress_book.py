from collections import UserDict
from typing import Union





class Field:
    def __init__(self, value: str):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class AddressBook(UserDict):

    def add_contact(self, name: Name, phone: Phone = None):
        contact = Record(name=name, phone=phone)
        self.data[name.value] = contact

    def add_record(self, record: "Record"):
        self.data[record.name.value] = record

    def find_contact(self, attribute, value):


    def change_contact(self, name, old_number, new_number):
        try:
            # self.data[name].replace(old_number)
            self.data[name].update({name: new_number})
        except ValueError:
            return f"{old_number} doesen't exists in book"

class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name: Name = name
        self.phones = [phone] if phone is not None else []

    # def __repr__(self):
    #     return f"{self.name.value}: {' '.join(phone.value for phone in self.phones)}"

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, old_number: Phone, new_number: Phone):
        try:
            self.phones.remove(old_number)
            self.phones.append(new_number)
        except ValueError:
            return f"{old_number} doesn't exists in book"

    def delite_phone(self, phone_number: Phone):

        try:
            self.phones.remove(phone_number)
        except ValueError:
            return f"{phone_number} doesn't exists in book"



