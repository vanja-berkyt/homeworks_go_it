



def hello_parser(user_input :str):
    return "hello", []


def add_parser(user_input :str):
    args = user_input.lstrip("add ")
    name, phone = args.split(" ")
    if name == "" or phone == "":
        raise ValueError("bad input")
    else:
        return "add", [name, phone]


def change_parser(user_input :str):
    args = user_input.lstrip("change ")
    name, phone = args.split(" ")
    if name == "" or phone == "":
        raise ValueError("bad input")
    else:
        return "change", [name, phone]

def phone_parser(user_input :str):
    name = user_input.lstrip("phone ")
    if name == "":
        raise ValueError("bad input")
    else:
        return "phone", [name]


def show_all_parser(user_input :str):
    if user_input == "show all":
        return "exit", []
    else:
        raise ValueError("bad input")


def good_bye_parser(user_input :str):
    for item in ["good bye ", "close ", "exit "]:
        if item == user_input:
            return "exit", []
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


def parse_user_input(user_input :str):
    for command in command_parser.keys():
        normalaised_input = " ".join(list(filter(lambda x: x != "", user_input.lower().split(" "))))
        normalaised_input = normalaised_input.ljust(len(normalaised_input) + 1, "")
        if normalaised_input.startswith(command + " "):
            parser = command_parser.get(command)
            return parser(user_input)
        else:
            raise ValueError("Unknown command")
