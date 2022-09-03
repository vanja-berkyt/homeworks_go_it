import datetime
import re
from collections import UserDict


class Field:
    def __init__(self, value: str):
        self._value = None
        self.value = value

    def __repr__(self):
        return self._value

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    @property
    def value(self) -> datetime.datetime:
        return self._value

    @Field.value.setter
    def value(self, value):
        self._value = value


class Phone(Field):
    # def __init__(self, value):
    #     super().__init__(value)
    #     self.value = self._value

    @property
    def value(self) ->str:
        return self._value

    @Field.value.setter
    def value(self, value):
        new_value = re.findall(r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}", value)
        for i in new_value:
            new_value = i
            if len(value >= 9) and len(new_value > 0):
                self._value = new_value
            else:
                self._value = None

class Birthday(Field):
    @property
    def value(self) -> datetime.datetime.date:
        return self._value

    @value.setter
    def value(self, value):
        self._value = datetime.datetime.strptime(value, "%d-%m-%y")   # додати перевірку

    def __repr__(self):
        return datetime.datetime.strftime(self._value, "%d-%m-%y")

class AddressBook(UserDict):

    __items_per_page = None

    def items_per_page(self, value):
        self.__items_per_page = value

    __items_per_page = property(fget=None, fset=items_per_page)


    def add_contact(self, name: Name, phone: Phone = None):
        contact = Record(name=name, phone=phone)
        self.data[name.value] = contact

    def add_record(self, record: "Record"):
        self.data[record.name.value] = record

    def find_by_name(self, name):
        try:
            return self.data[name]
        except KeyError:
            return None


    def find_by_phone(self, phone):
        for record in self.data.values():
            if phone in [number.values for number in record.phones]:
                return record
        return None

    def __iter__(self):
        self.page = 0
        return self

    def __next__(self):
        records = list(self.data.items())
        start_index = self.page * self.__items_per_page
        end_index = (self.page + 1) * self.__items_per_page
        self.page += 1

        if len(records) > len(end_index):
            to_retorn = records[start_index : end_index]
        else:
            if len(records) < len(start_index):
                to_retorn = records[start_index : len(records)]
            else:
                to_retorn = records[:-1]
        return [{record[1] : record[0]} for record in to_retorn]


def _now():
    datetime.datetime.today()


def _create_date(year, month, day):
    return datetime.datetime(year=year, month=month,day=day).date()


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name: Name = name
        self.phones = [phone] if phone is not None else []
        self.birthday = birthday

    def days_to_birthday(self):
        now = _now()
        if self.birthday is not None:
            birthday: datetime.datetime.date = self.birthday.value.date()
            next_birthday = _create_date(year=now.year, month=birthday.month,day=birthday.day)
            if birthday < next_birthday:
                next_birthday = _create_date(year=birthday.year+1, month=birthday.month,day=birthday.day)
            return (next_birthday - birthday).day
        return None

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
