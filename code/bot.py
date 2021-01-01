import re
import sys

CONTACTS = dict()


# Decorator to handle Exceptions
def input_error(func):
    def decorated_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(f"{func.__name__} got KeyError")
        except ValueError:
            print(f"{func.__name__} got KeyError")
        except IndexError:
            print(f"{func.__name__} got IndexError")
        except KeyboardInterrupt:
            print(f"{func.__name__} got KeyboardInterrupt")
        except TypeError:
            print(f"{func.__name__} got TypeError")
        except Exception as e:
            print(f"{func.__name__} got {e}")

    return decorated_function


@input_error
def good_bye():
    return "Good bye!"


@input_error
def hello():
    return "How can I help you?"


# Output all CONTACTS dictionary
@input_error
def show_all():
    if CONTACTS:
        return '\n'.join(map(': '.join, CONTACTS.items()))
    else:
        return "No Contacts!"


# Add record to CONTACTS dictionary
@input_error
def add(str_to_parse):
    arr_parsed = str_to_parse.split(" ")
    CONTACTS[arr_parsed[1]] = arr_parsed[2]
    return f"Added new record to Contacts list\n" \
           f" {arr_parsed[1]}: {arr_parsed[2]}"


# Change contacts number in CONTACTS dictionary
@input_error
def change(str_to_parse):
    arr_parsed = str_to_parse.split(" ")
    if arr_parsed[1] in CONTACTS:
        CONTACTS[arr_parsed[1]] = arr_parsed[2]
        return f"Changed record in Contacts list\n" \
               f" {arr_parsed[1]}: {arr_parsed[2]}"
    else:
        return f"No such Contact Name: {arr_parsed[1]}"


# Output user phone by username
@input_error
def phone(str_to_parse):
    arr_parsed = str_to_parse.split(" ")
    if arr_parsed[1] in CONTACTS:
        return f"Username {arr_parsed[1]} has number {CONTACTS[arr_parsed[1]]}"
    else:
        return f"No such Contact Name: {arr_parsed[1]}"


# Main func
@input_error
def main():
    while True:
        x = str(input("$> "))

        if re.match("close", x) or \
                re.match("exit", x) or \
                re.match("good bye", x):
            print(good_bye())
            sys.exit(0)

        elif re.match("hello", x):
            print(hello())

        elif re.match("show all", x):
            print(show_all())

        elif re.match("add [0-9a-zA-Z]+ [0-9]+$", x):
            print(add(x))

        elif re.match("change [0-9a-zA-Z]+ [0-9]+$", x):
            print(change(x))

        elif re.match("phone [0-9a-zA-Z]+$", x):
            print(phone(x))

        else:
            print("Please enter valid command!")


if __name__ == '__main__':
    while True:
        main()
