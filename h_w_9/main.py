from hendlers import handlers, unknown_handler
# from parser import parse_user_input


def input_handler(func):
    def wrapper(user_input):
        try:
            return func(user_input)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except Exception:
            raise SystemExit("Good bye!")
    return wrapper


@input_handler
def hello_parser(user_input :str):
    return "hello", []


@input_handler
def add_parser(user_input :str):
    args = user_input.lstrip("add ")
    name, phone = args.split(" ")
    if name == "" or phone == "":
        raise ValueError("bad input")
    else:
        return "add", [name, phone]


@input_handler
def change_parser(user_input :str):
    args = user_input.lstrip("change ")
    name, phone = args.split(" ")
    if name == "" or phone == "":
        raise ValueError("bad input")
    else:
        return "change", [name, phone]


@input_handler
def phone_parser(user_input :str):
    name = user_input.lstrip("phone ")
    if name == "":
        raise ValueError("bad input")
    else:
        return "phone", [name]

@input_handler
def show_all_parser(user_input :str):
    if user_input == "show all":
        return "show all", []
    else:
        raise ValueError("bad input")

@input_handler
def good_bye_parser(user_input :str):
    if user_input in ["good bye", "close", "exit"]:
        return "good bye", []
    else:
        raise ValueError("bad input")


command_parser = {
                   "hello": hello_parser,
                   "add": add_parser,
                   "change": change_parser,
                   "phone": phone_parser,
                   "show all": show_all_parser,
                   "good bye": good_bye_parser,
                   "close": good_bye_parser,
                   "exit": good_bye_parser
                   }

@input_handler
def parse_user_input(user_input :str):
    for command in command_parser.keys():
        normalaised_input = " ".join(list(filter(lambda x: x != "", user_input.lower().split(" "))))
        normalaised_input = normalaised_input.ljust(len(normalaised_input), " ")
        if normalaised_input.startswith(command):
            parser = command_parser.get(command)
            return parser(normalaised_input)

    raise ValueError("Unknown command")




def main():
    while True:
        user_input = input("Command: ")
        result = parse_user_input(user_input)
        if len(result) != 2:
            print(result)
            continue
        command, arguments = result
        command_handler = handlers.get(command, unknown_handler)
        try:
            command_response = command_handler(*arguments)
            print(command_response)
        except SystemExit as e:
            print(str(e))
            break

if __name__ == "__main__":
    main()


# def input_error(func):
#     def inner(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except Exception as e:
#             print(e)
#             print(f'input correct data')
#
#     return inner
#
#
# def hello():
#     print("How can I help you?")
#
# def add(name, phone_number):
#     dict.update({name : phone_number})
#
# def change(name, phone_number):
#     for key, value in dict.items():
#         if key == name:
#             dict[name] = phone_number
#
# def phone(name, phone_number=None):
#     print(dict.get(name))
#
# def show_all(name=None, phone_number=None):
#     for key, value in dict.items():
#         print(key, value)
#
# def good_bye(name=None, phone_number=None):
#     print("Good bye!")
#
# def input_parser(line: str):
#     line.lower()
#     words = line.split(' ')
#     def inner(index_in_line):
#         nonlocal words
#         return words[index_in_line]
#     return inner
#
#
#     # try:
#     #
#     #     # print(f"comand {words[0]}, name: {words[1]}, phone: {words[2]}")
#     #     return words
#     # except:
#     #     print("input 3 words")
#
#
# com = "0"
# while com != ".":
#     input_word = input_parser(input())
#     com = input_word(0)
#     name = input_word(1)
#     phone_number = input_word(2)
#
#     comand = {"hello": hello, "add": add, "change": change, "phone": phone, "show_all": show_all,
#               "good_bye": good_bye,
#               ".": good_bye, "close": good_bye, "exit": good_bye}
#     comand[com](name, phone_number)
#     print(name, phone_number)
