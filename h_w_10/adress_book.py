from collections import UserDict
from typing import Union


class AddressBook(UserDict):

    def add_contact(self, name: str, phone: Union[str, list] = None):
        contact = Record(name=name, phone=phone)
        self.data[name] = contact

    def change_contact(self, name, old_number, new_number):
        try:
            # self.data[name].replace(old_number)
            self.data[name].update({name: new_number})
        except ValueError:
            return f"{old_number} doesen't exists in book"


class Record:
    def __init__(self, name: str, phone: Union [str, list] = None):
        self.name = name
        self.phones = [phone] if phone is not None else []

    def add_phone(self, phone_number: str):
        self.phones.append(phone_number)

    def change_phone(self, old_number, new_number):
        try:
            self.phones.remove(old_number)
            self.phones.append(new_number)
        except ValueError:
            return f"{old_number} doesen't exists in book"

    def delite_phone(self,phone_number: str):

        try:
            self.phones.remove(phone_number)
        except ValueError:
            return f"{phone_number} doesen't exists in book"



class Field:
    def __init__(self, value: str):



class Name(Field):
    pass
class Phone(Field):
    pass
