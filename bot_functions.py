from address_book import Record, AddressBook, Notes, BookForNotes
from validation_functions.validation import input_error
from validation_functions.validation import name_validation, phone_validation

########################### ADD CONTACT ##################################

@name_validation
@phone_validation
@input_error
def add_contact(name: str, phone_number: str, book: AddressBook) -> str:
    #очищаємо пробіли в імені, якщо потрібно
    name = name.strip()

    #шукаємо запис в книзі контактів
    record = book.find_record(name)

    if record is not None:
        #якщо контакт вже є, додаємо новий номер телефону
        try:
            record.add_phone(phone_number)
            return f"Phone number {phone_number} added to {name}."
        except ValueError as e:
            return f"Error: {str(e)}"
    else:
        #якщо контакт не знайдений, створюємо новий
        try:
            record = Record(name)
            record.add_phone(phone_number)
            book.add_record(record)
            return f"Contact {name} added with phone number {phone_number}."
        except ValueError as e:
            return f"Error: {str(e)}"

########################### PHONE ##################################

@input_error
def change_phone(args, book):
    """Функція для зміни телефону."""
    if len(args) < 2:
        return "Error: Two arguments required: name, new_phone."

    name, new_phone = args[0], args[1]
    record = book.find_record(name)

    if record:
        try:
            #перевіряємо наявність старого номера і редагуємо його
            old_phone = record.phones[0].phone if record.phones else None  #беремо перший номер телефону
            if old_phone:
                #редагуємо телефон
                record.edit_phone(old_phone, new_phone)
                return f"Phone number for {name} changed from {old_phone} to {new_phone}."
            else:
                return f"No phone number found for {name}."
        except ValueError as e:
            return f"Error: {e}"  #якщо виникла помилка при редагуванні
    else:
        return f"Contact with name {name} not found."

@input_error
def show_phone(name: str, book: AddressBook) -> str:
    if not name:
        return "Invalid command. Usage: phone [name]"

    name = name.strip() #очищаємо пробіли в імені, якщо потрібно

    #шукаємо контакт в книзі
    record = book.find_record(name)

    if record:
        if record.phones:
            phone_numbers = "; ".join(str(p.phone) for p in record.phones)
            return f"Phone numbers for {name.capitalize()}: {phone_numbers}"
        else:
            return f"Contact {name.capitalize()} has no phone numbers."
    else:
        return f"Contact with name {name.capitalize()} not found."

########################### SHOW ALL ##################################

@input_error
def show_all(book):
    if not book.data: #перевіряємо чи адресна книга порожня
        return "No contacts found."
    return "\n".join(str(record) for record in book.data.values()) #повертаємо всі записи в адресній книзі

########################### BIRTHDAYS ##################################

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

########################### EMAILS ##################################

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

########################### RECORDS ##################################

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


########################### NOTES ##################################
  
@input_error
def show_note(name, book):
    record = book.find_record(name)
    
    if not record:
        return f"Error: Contact with name {name} not found."
    
    #перевірка, чи існує об'єкт notes і чи це клас BookForNotes
    if not isinstance(record.notes, BookForNotes) or not record.notes.data:
        return f"Error: No valid notes found for {name}."
    
    #отримуємо всі нотатки без квадратних дужок
    notes = record.notes.show_notes().replace("[", "").replace("]", "")  #видаляємо квадратні дужки
    
    #збираємо теги для всіх нотаток
    all_tags = set()
    for note in record.notes.data.values():
        if isinstance(note, Notes):  #перевірка чи це об'єкт класу Notes
            all_tags.update(note.tag)  #додаємо теги з нотатки
    
    #якщо теги є, ми їх покажемо, інакше покажемо "No tags"
    tags = ", ".join(sorted(all_tags)) if all_tags else "No tags"
    
    #повертаємо більш читабельний формат
    return f"Notes for {name}: {notes} | Tags: {tags}"

@input_error
def add_note(args, book):
    """Функція для додавання нотатки."""
    name, note_text = args[0], " ".join(args[1:])
    record = book.find_record(name)
    
    if not record:
        return f"Contact with name {name} not found."

    try:
        #перевірка чи notes — правильного типу
        if not isinstance(record.notes, BookForNotes):
            record.notes = BookForNotes()

        #створення об'єкта Notes
        note = Notes(note_text)

        #додавання нотатки
        record.notes.add_note(note)

        return f"Note for {name} added: {note_text}."
    except ValueError as e:
        return str(e)
    
@input_error
def remove_note(name, note_text, book):
    """Функція для видалення нотатки."""
    
    record = book.find_record(name)  # Знаходимо контакт за ім'ям
    
    if record:
        # Перевіряємо всі нотатки
        deleted = False
        for note_id, note in record.notes.data.items():
            if note_text in note.notes:  # Якщо текст нотатки містить зазначений текст
                if record.notes.delete_note(note_id):  # Видаляємо цю нотатку за її id
                    deleted = True
                    break
        
        if deleted:
            return f"Note for {name} removed."
        else:
            return f"Error: No note found matching '{note_text}' for {name}."
    else:
        return f"Contact with name {name} not found."
 
@input_error
def edit_note(args, book):
    """Функція для редагування нотатки."""
    name, old_note, new_note = args[0], args[1], args[2]
    record = book.find_record(name)
    
    if record:
        try:
            #редагуємо нотатку в записі
            if record.notes.edit_note(old_note, new_note):  #перевіряємо, чи нотатка знайдена і змінена
                return f"Note for {name} changed from '{old_note}' to '{new_note}'."
            else:
                return f"Error: No note found matching '{old_note}' for {name}."
        except ValueError as e:
            return str(e)
    else:
        return f"Contact with name {name} not found."
    

@input_error
def add_tag(name, tag, book):
    record = book.find_record(name)
    
    if not record:
        return f"Error: Contact with name {name} not found."
    
    if not isinstance(record.notes, BookForNotes) or not record.notes.data:
        return f"Error: No valid notes found for {name}."
    
    #перевіряємо, чи є нотатки
    if not record.notes.data:
        return f"Error: No notes found for {name}."
    
    #отримуємо останню нотатку
    last_note = list(record.notes.data.values())[-1]

    try:
        #додаємо тег до останньої нотатки
        last_note.add_tag(tag)
        return f"Tag '{tag}' added to note: {last_note.notes}"
    except Exception as e:
        return f"Failed to add tag: {e}"