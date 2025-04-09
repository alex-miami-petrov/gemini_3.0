from address_book import Record, AddressBook
from validation_functions.validation import input_error
from validation_functions.validation import name_validation, phone_validation

@name_validation
@phone_validation
@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find_record(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

#############################################################

@name_validation
@phone_validation
@input_error
def edit_phone(args, book):
    """Функція для зміни контакту."""
    name, phone = args[0], args[1]
    record = book.find_record(name)
    if record:
        try:
            #редагуємо номер телефону
            record.edit_phone(record.phones[0].phone, phone)
            return f"Phone number for {name} changed to {phone}."
        except ValueError as e:
            return str(e)
    else:
        return f"Contact with name {name} not found."

#############################################################

@name_validation
@phone_validation
@input_error
def show_phone(name, book):
    record = book.find_record(name)
    if record:
        #повертаємо перший номер телефону з запису
        return f"Phone number for {name}: {record.phones[0]}"
    else:
        return f"Contact with name {name} not found."

#############################################################

@input_error
def show_all(book):
    if not book.data: #перевіряємо чи адресна книга порожня
        return "No contacts found."
    return "\n".join(str(record) for record in book.data.values()) #повертаємо всі записи в адресній книзі

@input_error
def add_birthday(args, book):
    name, birthday = args[0], args[1]
    record = book.find_record(name)
    if record:
        try:
            #додаємо дату народження до запису
            record.add_birthday(birthday)
            return f"Birthday for {name} added: {birthday}."
        except ValueError as e:
            return str(e)
    else:
        return f"Contact with name {name} not found."

@input_error
def show_birthday(args, book):
    """Функція для виведення дня народження контакту."""
    if not args:
        return "Error: No name provided."
    
    #перетворюємо `args` на список, якщо це просто рядок
    if isinstance(args, str):
        args = [args]

    name = args[0]
    record = book.find_record(name)
    
    if record:
        if record.birthday is None:
            return f"No birthday found for {name}."
        return f"Birthday for {name}: {record.birthday}"
    else:
        return f"Contact with name {name} not found."

@input_error
def birthdays(book):
    """Функція для виведення майбутніх днів народження."""
    upcoming_birthdays = book.upcoming_birthdays()  #використовуємо вже готовий метод
    if not upcoming_birthdays:
        return "No upcoming birthdays."
    
    return "\n".join([f"For {entry['name']}: congratulation date is {entry['congratulation_date']}" for entry in upcoming_birthdays])

@input_error
def all_birthdays(book, number_of_days):
    """Функція для виведення днів народження в заданий період."""
    birthdays = book.birthdays_pack(days=number_of_days)
    if not birthdays:
        return "🎈 Немає днів народження в найближчі дні."
    return "\n".join([f"{name}: {birthday}" for name, birthday in birthdays.items()])

@input_error
def add_email(args, book):
    name, email = args[0], args[1]
    record = book.find_record(name)
    if record:
        try:
            #додаємо мейл до запису
            record.add_email(email)
            return f"Email for {name} added: {email}."
        except ValueError as e:
            return str(e)
    else:
        return f"Contact with name {name} not found."
    
@input_error
def show_email(name, book):
    record = book.find_record(name)
    if record:
        if record.emails:  #перевіряємо, чи є email-и
            emails = "; ".join(str(email) for email in record.emails)  #об'єднуємо всі email-и
            return f"Emails for {name}: {emails}"
        else:
            return f"No email found for {name}."
    else:
        return f"Contact with name {name} not found."

@input_error
def change_email(args, book):
    """Функція для зміни email."""
    if len(args) != 3:
        return "Error: Three arguments required: name, old_email, new_email."

    name, old_email, new_email = args[0], args[1], args[2]
    record = book.find_record(name)

    if record:
        try:
            # Редагуємо email
            record.edit_email(old_email, new_email)
            return f"Email for {name} changed from {old_email} to {new_email}."
        except ValueError as e:
            return f"Error: {e}"  # Покажемо помилку, якщо email не знайдений чи є інша проблема
    else:
        return f"Contact with name {name} not found."
    
@input_error
def find_record(name, book):
    """Функція для пошуку контакту."""
    record = book.find_record(name)
    if record:
        return str(record)
    else:
        return f"Contact with name {name} not found."
    
@input_error
def remove_record(name, book):
    """Функція для видалення контакту."""
    record = book.find_record(name)
    if record:
        book.remove_record(name)
        return f"Contact {name} removed."