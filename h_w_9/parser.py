


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




