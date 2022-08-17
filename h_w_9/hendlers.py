
from typing import Dict, Callable
from phone_book import book

def hello(*args):
    print("How can I help you?")

def add(name:str, phone_number:str):
    if book.get(name) is None:
        book.update({name : phone_number})
        return "Number was added"
    else:
        raise ValueError("number exists")

def change(name, phone_number):
    if book.get(name) is not None:
        book[name] = phone_number
        return "number was changed!"
    else:
        raise KeyError("number dos't exists")

def phone(name):
    number = book.get(name)
    if number is not None:
        return f"user number is {number}"
    else:
        raise ValueError


def show_all(*args):
    contacts = "\n".join(f'{name}: {number}' for (name, number) in book.items())
    form_contacts = "number does not exists" if contacts == "" else contacts
    return form_contacts

def good_bye(*args):
    raise SystemExit("Good bye!")

def unknown_handler(*args):
    raise ValueError("Command is not valid!")


handlers: Dict[str, Callable] =  {
                   "hello": hello,
                   "add": add,
                   "change": change,
                   "phone": phone,
                   "show all": show_all,
                   "good bye": good_bye,
                   "close": good_bye,
                   "exit": good_bye
                   }
