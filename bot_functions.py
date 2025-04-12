from address_book import Record, AddressBook, Notes, BookForNotes
from validation_functions.validation import input_error
from validation_functions.validation import name_validation, phone_validation


@name_validation
@phone_validation
@input_error
def add_contact(name: str, phone_number: str, book: AddressBook) -> str:
    name = name.strip()

    
    record = book.find_record(name)
    if record is not None:
        try:
            record.add_phone(phone_number)
            return f"Phone number {phone_number} added to {name}."
        except ValueError as e:
            return f"Error: {str(e)}"
    else:
        try:
            record = Record(name)
            record.add_phone(phone_number)
            book.add_record(record)
            return f"Contact {name} added with phone number {phone_number}."
        except ValueError as e:
            return f"Error: {str(e)}"


@input_error
def change_phone(args, book):
    """Функція для зміни телефону."""
    if len(args) < 2:
        return "Error: Two arguments required: name, new_phone."

    name, new_phone = args[0], args[1]
    record = book.find_record(name)

    if record:
        try:
            old_phone = record.phones[0].phone if record.phones else None  
            if old_phone:
                record.edit_phone(old_phone, new_phone)
                return f"Phone number for {name} changed from {old_phone} to {new_phone}."
            else:
                return f"No phone number found for {name}."
        except ValueError as e:
            return f"Error: {e}" 
    else:
        return f"Contact with name {name} not found."

@input_error
def show_phone(name: str, book: AddressBook) -> str:
    if not name:
        return "Invalid command. Usage: phone [name]"

    name = name.strip()

    
    record = book.find_record(name)

    if record:
        if record.phones:
            phone_numbers = "; ".join(str(p.phone) for p in record.phones)
            return f"Phone numbers for {name.capitalize()}: {phone_numbers}"
        else:
            return f"Contact {name.capitalize()} has no phone numbers."
    else:
        return f"Contact with name {name.capitalize()} not found."


@input_error
def show_all(book):
    if not book.data:
        return "No contacts found."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book):
    name, birthday = args[0], args[1]
    record = book.find_record(name)
    if record:
        try:
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
    upcoming_birthdays = book.upcoming_birthdays()
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
        if record.emails:
            emails = "; ".join(str(email) for email in record.emails) 
            return f"Emails for {name}: {emails}"
        else:
            return f"No email found for {name}."
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
            record.edit_email(old_email, new_email)
            return f"Email for {name} changed from {old_email} to {new_email}."
        except ValueError as e:
            return f"Error: {e}"
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


@input_error
def show_note(name, book):
    record = book.find_record(name)
    
    if not record:
        return f"Error: Contact with name {name} not found."
    
    if not isinstance(record.notes, BookForNotes) or not record.notes.data:
        return f"Error: No valid notes found for {name}."
    
    notes = record.notes.show_notes().replace("[", "").replace("]", "")  
    
    all_tags = set()
    for note in record.notes.data.values():
        if isinstance(note, Notes):
            all_tags.update(note.tag)
    
    tags = ", ".join(sorted(all_tags)) if all_tags else "No tags"
    
    return f"Notes for {name}:\n{notes}\nTags: {tags}"


@input_error
def add_note(args, book):
    """Функція для додавання нотатки."""
    if len(args) < 3:
        return "Usage: add-note <Contact Name> <Title> <Note Text>"

    name = args[0]
    title = args[1]
    note_text = " ".join(args[2:])

    record = book.find_record(name)
    
    if not record:
        return f"Contact with name '{name}' not found."

    try:
        if not isinstance(record.notes, BookForNotes):
            record.notes = BookForNotes()

        note = Notes(title, note_text)
        record.notes.add_note(note)

        return f"Note added to {name}:\n{note}"
    except ValueError as e:
        return str(e)
    
@input_error
def remove_note(name, title, book):
    """Функція для видалення нотатки за заголовком."""
    
    record = book.find_record(name)
    
    if record:
        deleted = False
        for note_id, note in record.notes.data.items():
            if note.title == title:
                if record.notes.delete_note(note_id):  
                    deleted = True
                    break
        
        if deleted:
            return f"Note with title '{title}' for {name} removed."
        else:
            return f"Error: No note found with title '{title}' for {name}."
    else:
        return f"Contact with name '{name}' not found."

 
@input_error
def edit_note(args, book):
    """Функція для редагування тексту нотатки за її заголовком."""
    if len(args) < 3:
        return "Usage: change-note <Contact Name> <Title> <New Note Text>"

    name, title = args[0], args[1]
    new_note_text = " ".join(args[2:])

    record = book.find_record(name)
    if not record:
        return f"Contact with name '{name}' not found."

    if not isinstance(record.notes, BookForNotes):
        return f"{name} has no notes to edit."

    if record.notes.edit_note(title, new_note_text):
        return f"Note with title '{title}' for {name} updated successfully."
    else:
        return f"No note found with title '{title}' for {name}."
    

@input_error
def add_tag(name, tag, book):
    record = book.find_record(name)
    
    if not record:
        return f"Error: Contact with name {name} not found."
    
    if not isinstance(record.notes, BookForNotes) or not record.notes.data:
        return f"Error: No valid notes found for {name}."
    
    if not record.notes.data:
        return f"Error: No notes found for {name}."
    
    last_note = list(record.notes.data.values())[-1]

    try:
        last_note.add_tag(tag)
        return f"Tag '{tag}' added to note: {last_note.notes}"
    except Exception as e:
        return f"Failed to add tag: {e}"


@input_error
def add_address(args, book) -> str:
    """Функція для додавання адреси."""
    if len(args) < 4:
        return "Error: Not enough arguments for adding address. Format: add-address <name> <city> <street> <house>"
    
    name = args[0]
    address = ", ".join(args[1:])

    record = book.find_record(name)
    if not record:
        return f"Contact '{name}' not found."
    
    record.add_address(address)
    return f"Address for '{name}' added successfully."                                    

@input_error
def show_address(name: str, book) -> str:
    record = book.find_record(name)
    if record:
        if record.address:
            return f"Address for {name}: {record.address}"
        else:
            return f"No address found for {name}."
    else:
        return f"No contact found with name {name}."

@input_error   
def change_address(args, book: AddressBook) -> str:
    if len(args) < 5:
        return "Error: Please provide name, city, street, and house."
    
    name, city, street, house = args[0], args[1], args[2], args[3]
    record = book.find_record(name)
    
    if record:
        record.change_address(city, street, house)
        return f"Address for {name} changed to: {city}, {street}, {house}"
    else:
        return f"No contact found with name {name}."