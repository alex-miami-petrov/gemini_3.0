from bot_functions import add_contact, edit_phone, show_phone, show_all, add_birthday, show_birthday, birthdays, all_birthdays, add_email, show_email, change_email, find_record, remove_record
from parse import parse_input
from address_book import AddressBook  #додали імпорт класу AddressBook
from validation_functions.validation import name_validation, phone_validation, input_error
from file_func import save_data, load_data  #додали імпорт функцій для роботи з файлами

def main():
    book = load_data()
    if not book:
        book = AddressBook() #якщо адресна книга пуста, створюємо нову
    
    print("Welcome to the assistant bot!")
    print("You can use the following commands:")
    print("add, change, phone, all, add-birthday, show-birthday, birthdays, add-email, show-email, change-email, hello, close, exit.")

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            print("Error: Please enter a command.")
            continue

        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print("Invalid command. Available commands: add, change, phone, all, add-birthday, show-birthday, birthdays, add-email, show-email, change-email, hello, close, exit.")
            continue

        if command in ["close", "exit"]:
            save_data(book) #зберігаємо дані перед виходом
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) < 2:
                print("Error: Please provide both name and phone number.")
            else:
                print(add_contact(args, book))  #передаємо book замість contacts
        elif command == "change-phone":
            if len(args) < 2:
                print("Error: Please provide both name and phone number.")
            else:
                print(edit_phone(args, book))  #передаємо book замість contacts
        elif command == "show-contact":
            if not args:
                print("Error: Please provide a name to find the contact.")
            else:
                print(find_record(args[0], book))
        elif command == "remove":
            if not args:
                print("Error: Please provide a name to remove the contact.")
            else:
                print(remove_record(args[0], book))
        elif command == "phone":
            if not args:
                print("Error: Please provide a name to find the phone number.")
            else:
                print(show_phone(args[0], book))  #передаємо book замість contacts
        elif command == "all":
            print(show_all(book))  #передаємо book замість contacts
        elif command == "add-birthday":
            if len(args) < 2:
                print("Error: Please provide both name and birthday.")
            else:
                print(add_birthday(args, book)) #передаємо book замість contacts
        elif command == "show-birthday":
            if not args:
                print("Error: Please provide a name to find the birthday.")
            else:
                print(show_birthday(args[0], book)) #передаємо book замість contacts
        elif command == "birthdays":
            print(birthdays(book)) #передаємо book замість contacts
        elif command == "all-birthdays":
            if len(args) < 1:
                print("Error: Please provide the number of days.")
            else:
                try:
                    number_of_days = int(args[0])
                    result = book.birthdays_pack(number_of_days)  # book — це AddressBook
                    if not result:
                        print("No birthdays found.")
                    else:
                        print(f"In {number_of_days} days the birthdays will be for:")
                        for name, bday in result.items():
                            print(f"{name}: {bday}")
                except ValueError:
                    print("Error: Please provide a valid number of days.")
        elif command == "add-email":
            if len(args) < 2:
                print("Error: Please provide both name and email.")
            else:
                print(add_email(args, book))
        elif command == "show-email":
            if not args:
                print("Error: Please provide a name to find the email.")
            else:
                print(show_email(args[0], book))
        elif command == "change-email":
            if len(args) < 2:
                print("Error: Please provide both name and email.")
            else:
                print(change_email(args, book))
        else:
            print("Invalid command. Available commands: add, change, phone, all, add-birthday, show_birthday, birthdays, hello, close, exit.")
if __name__ == "__main__":
    main()