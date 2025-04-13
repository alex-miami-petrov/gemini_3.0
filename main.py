from bot_functions import *
from parse import parse_input
from address_book import AddressBook
from validation_functions.validation import name_validation, phone_validation, input_error
from file_func import save_data, load_data
from rich_func import show_commands
from guess_command import *

from prompt_toolkit import prompt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory



def handle_hello(args, book):
    print("How can I help you?")

def handle_add(args, book):
    if len(args) < 2:
        print("Error: Please provide both name and phone number.")
    else:
        print(add_contact(args, book))

def handle_change_phone(args, book):
    if len(args) < 2:
        print("Error: Please provide both name and phone number.")
    else:
        print(change_phone(args, book))

def handle_show_contact(args, book):
    if not args:
        print("Error: Please provide a name to find the contact.")
    else:
        print(find_record(args[0], book))

def handle_remove(args, book):
    if not args:
        print("Error: Please provide a name to remove the contact.")
    else:
        print(remove_record(args[0], book))

def handle_show_phones(args, book):
    if not args:
        print("Error: Please provide a name to find the phone number.")
    else:
        print(show_phone(args[0], book))

def handle_all(args, book):
    print(show_all(book))

def handle_add_address(args, book):
    if len(args) < 4:
        print("Error: Please provide both name and full address (city, street, house).")
    else:
        print(add_address(args, book))

def handle_show_address(args, book):
    if not args:
        print("Error: Please provide a name to find the address.")
    else:
        print(show_address(args[0], book))

def handle_change_address(args, book):
    if len(args) < 4:
        print("Error: Please provide name, city, street, and house.")
    else:
        print(change_address(args, book))

def handle_add_birthday(args, book):
    if len(args) < 2:
        print("Error: Please provide both name and birthday.")
    else:
        print(add_birthday(args, book))

def handle_show_birthday(args, book):
    if not args:
        print("Error: Please provide a name to find the birthday.")
    else:
        print(show_birthday(args[0], book))

def handle_birthdays(args, book):
    print(birthdays(book))

def handle_all_birthdays(args, book):
    if len(args) < 1:
        print("Error: Please provide the number of days.")
    else:
        try:
            number_of_days = int(args[0])
            result = book.birthdays_pack(number_of_days)
            if not result:
                print("No birthdays found.")
            else:
                print(f"In {number_of_days} days the birthdays will be for:")
                for name, bday in result.items():
                    print(f"{name}: {bday}")
        except ValueError:
            print("Error: Please provide a valid number of days.")

def handle_add_email(args, book):
    if len(args) < 2:
        print("Error: Please provide both name and email.")
    else:
        print(add_email(args, book))

def handle_show_email(args, book):
    if not args:
        print("Error: Please provide a name to find the email.")
    else:
        print(show_email(args[0], book))

def handle_change_email(args, book):
    if len(args) < 2:
        print("Error: Please provide both name and email.")
    else:
        print(change_email(args, book))

# def handle_add_note(args, book):
#     print(add_note(args, book))
#     response = input("Do you want to add some tags? y/n ").strip().lower()
#     if response == "y":
#         tags = input("Enter tags separated by commas: ").strip().split(",")
#         for tag in tags:
#             add_tag(args[0], tag.strip(), book)
#         print("Tags added.")
#     else:
#         print("No tags added.")

def handle_add_note(args, book):
    while True:
        if len(args) < 3:
            print("Error: Please provide name, title and note.")
            try_again = input("Do you want to try again? y/n ").strip().lower()
            if try_again == "y":
                new_command = input("Enter a command: ").strip()
                parts = new_command.split()
                if parts and parts[0] == "add-note":
                    args = parts[1:]
                    continue
                else:
                    print("Invalid command. Returning to main menu.")
                    return
            else:
                print("Aborting note addition.")
                return
        else:
            print(add_note(args, book))
            response = input("Do you want to add some tags? y/n ").strip().lower()
            if response == "y":
                tags = input("Enter tags separated by commas: ").strip().split(",")
                for tag in tags:
                    add_tag(args[0], tag.strip(), book)
                print("Tags added.")
            else:
                print("No tags added.")
            return

def handle_show_note(args, book):
    if not args:
        print("Error: Please provide a name to find the note.")
    else:
        print(show_note(args[0], book))

def handle_change_note(args, book):
    if len(args) < 3:
        print("Error: Please provide name, title and new note.")
    else:
        print(edit_note(args, book))

def handle_remove_note(args, book):
    if len(args) < 2:
        print("Error: Please provide both name and title of note.")
    else:
        print(remove_note(args[0], args[1], book))

def main():
    book = load_data()
    if not book:
        book = AddressBook()

    show_commands()

    completer_obj = get_completer()

    command_handlers = {
        "hello": handle_hello,
        "add": handle_add,
        "change-phone": handle_change_phone,
        "show-contact": handle_show_contact,
        "remove": handle_remove,
        "show-phones": handle_show_phones,
        "all": handle_all,
        "add-address": handle_add_address,
        "show-address": handle_show_address,
        "change-address": handle_change_address,
        "add-birthday": handle_add_birthday,
        "show-birthday": handle_show_birthday,
        "birthdays": handle_birthdays,
        "all-birthdays": handle_all_birthdays,
        "add-email": handle_add_email,
        "show-email": handle_show_email,
        "change-email": handle_change_email,
        "add-note": handle_add_note,
        "show-note": handle_show_note,
        "change-note": handle_change_note,
        "remove-note": handle_remove_note,
    }

    try:
        while True:
            user_input = prompt("Enter a command: ", completer=completer_obj, auto_suggest=AutoSuggestFromHistory()).strip()

            if not user_input:
                print("Error: Please enter a command.")
                continue

            try:
                command, *args = parse_input(user_input)
            except ValueError:
                print(f"Invalid command. Available commands: {', '.join(commands_list)}.")
                continue

            save_commands = [
                "add", "change-phone", "remove",
                "add-birthday", "add-email", "change-email",
                "add-note", "change-note", "remove-note", "add-address", "change-address"
            ]

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command in command_handlers:
                command_handlers[command](args, book)
            else:
                print(f"Invalid command. Available commands: {', '.join(commands_list)}.")

            if command in save_commands:
                save_data(book)

    except KeyboardInterrupt:
        print("\nSaving data and exiting...")
        save_data(book)
        print("Data saved. Good bye!")

if __name__ == "__main__":
    main()