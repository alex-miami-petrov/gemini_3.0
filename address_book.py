from collections import UserDict
from normalize import normalize_phone
from datetime import datetime, date
from birthdays_func import get_upcoming_birthdays
from all_birthdays_func import all_birthdays
from uuid import uuid4

class Field:
    """Базовий клас для полів запису (ім'я, телефон, email)"""
    pass

class Name(Field):
    """Клас для зберігання імені контакту"""
    def __init__(self, name):
        if not isinstance(name, str) or not name.replace(" ", "").isalpha(): #перевіряємо чи ім'я складається з букв та пробілів
            raise ValueError("Name must be a string containing only letters and spaces.") 
        self.name = name #зберігаємо ім'я

    def __str__(self):
        return self.name

class Phone(Field):
    """Клас для зберігання номера телефону"""
    def __init__(self, phone):
        if not isinstance(phone, str) or not phone.isdigit(): #перевіряємо чи номер складається з цифр
            raise ValueError("Phone number must be a string containing only digits.") 
        self.phone = normalize_phone(phone)  #нормалізуємо номер

    def __str__(self):
        return self.phone #повертаємо нормалізований номер

class Email(Field):
    """Клас для зберігання email"""
    def __init__(self, email):
        if not isinstance(email, str) or "@" not in email: #перевіряємо чи email є рядком та містить @
            raise ValueError("Email must be a valid string containing '@'.")
        self.email = email #зберігаємо email

    def __str__(self):
        return self.email
class Address(Field):
    """Клас для зберігання адреси"""
    def __init__(self, city: str, street: str, house: str, address: str = None):
        #неправильна частина була тут, тому потрібно без переписування параметрів
        if not isinstance(address, str): # we are checking if notes is a string
            raise ValueError("Add something to address.")
        self.city = city
        self.street = street
        self.house = house
        self.address = address #зберігаємо адресу

    def __str__(self):
        return f"{self.city}, {self.street}, {self.house}"

# class Contact:
#     def __init__(self, name: str):
#         self.data = {} #ініціалізуємо словник для зберігання адреси
#         self.address = None  # ініціалізація адреси як None

#     def add_address(self, city: str, street: str, house: str):
#         """Додає адресу до контакту"""
#         self.address = Address(city, street, house)

#     def get_address(self):
#         """Отримує адресу контакту"""
#         return str(self.address) if self.address else "No address"
    
class Notes(Field):
    """Клас для зберігання notes"""
    def __init__(self, title, notes, tag = None):
        if not isinstance(notes, str): # we are checking if notes is a string
            raise ValueError("Add something to notes.")
        self.id = str(uuid4()) #генеруємо унікальний id для нотатки
        self.title = title or "Untitled"
        self.notes = notes #зберігаємо notes
        self.tag = set(tag) if tag else set()

    def add_tag(self, tag):
        if not isinstance(tag, str): 
            raise ValueError("Tag must be a string.")
        self.tag.add(tag.lower())  # adding tags

    def remove_tag(self, tag):
        if tag in self.tag:
            self.tag.remove(tag.lower())

    def show_tags(self):
        if not self.tag:
            return "No tags"
        return ", ".join(tag for tag in self.tag)
    
    def __str__(self):
        # tags_str = ", ".join(self.tag) if self.tag else "No tags"
        # return f"Title: {self.title} | Note: {self.notes} | Tags: {tags_str}"
        parts = []
        if hasattr(self, "title") and self.title:
            parts.append(f"Title: {self.title}")
        if hasattr(self, "notes") and self.notes:
            parts.append(f"Text: {self.notes}")
        if self.tag:
            parts.append("Tags: " + ", ".join(sorted(self.tag)))
        return "\n".join(parts) if parts else "Empty Note"
    
class BookForNotes(UserDict):
    """Клас для зберігання нотаток"""
    def __init__(self):
        super().__init__() 
        self.data = {}  #ініціалізуємо словник для зберігання нотаток

    def add_note(self, notes):
        self.data[notes.id] = notes  #додаємо нотатку до словника

    def delete_note(self, note_id):
        return self.data.pop(note_id, None) is not None  #видаляємо нотатку з словника
    
    def find_note(self, note_id):
        return self.data.get(note_id, None)

    def edit_note(self, title, new_note_text):
        """Редагує текст нотатки за її заголовком, залишаючи заголовок незмінним."""
        for note in self.data.values():
            if note.title == title:  #шукаємо нотатку за її заголовком
                note.notes = new_note_text  #оновлюємо текст нотатки
                return True  #якщо нотатку знайдено і текст змінено
        return False  #якщо нотатку не знайдено
    
    def show_notes(self):
        """Повертає всі нотатки у форматі рядка"""
        if not self.data:
            return "No notes available."
        return "; ".join(str(note) for note in self.data.values())
    
    def __str__(self):
        return self.show_notes()

def __str__(self):
    if not self.data:
        return "No notes"
    return "\n".join(str(note) for note in self.data.values())
class Birthday(Field):
    """Клас для зберігання дати народження"""
    def __init__(self, birthday):
        if not isinstance(birthday, str): #перевіряємо чи дата є рядком
            raise ValueError("Birthday must be a string in the format 'YYYY-MM-DD'.")
        self.birthday = self._parse_date(birthday) #викликаємо метод для парсингу дати
        
    def _parse_date(self, birthday):
        """Парсить дату народження з рядка"""
        try:
            return datetime.strptime(birthday, "%Y-%m-%d").date() #повертаємо і перевіряємо чи дата у правильному форматі date
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        
    @property
    def date(self):
        """Властивість для доступу до дати народження"""
        return self.birthday

    def __str__(self):
        return self.birthday.strftime("%Y-%m-%d") #повертаємо дату у форматі YYYY-MM-DD

class Record:
    """Клас для зберігання інформації про контакт"""
    def __init__(self, name, address=None, birthday=None, notes=None):
        self.name = Name(name)
        self.phones = [] 
        self.emails = []
        self.birthday = birthday if birthday else None
        self.notes = notes if isinstance(notes, BookForNotes) else BookForNotes() #ініціалізуємо нотатки, якщо вони є
        self.address = address if address else None  #ініціалізуємо адресу, якщо вона є

    def add_phone(self, phone):
        """Додає номер телефону до запису"""
        phone = Phone(phone) if isinstance(phone, str) else phone
        if phone.phone not in [p.phone for p in self.phones]:  #перевіряємо, чи номер вже є
            self.phones.append(phone)
        else:
            raise ValueError(f"Phone {phone.phone} already exists.")

    def remove_phone(self, phone):
        """Видаляє номер телефону з запису"""
        normalized_phone = normalize_phone(phone)
        self.phones = [p for p in self.phones if p.phone != normalized_phone] #фільтруємо номери, залишаючи тільки ті, що не відповідають видаленому

    def edit_phone(self, old_phone: str, new_phone: str):
        """Редагує номер телефону"""
        if self.find_phone(old_phone):
            self.remove_phone(old_phone) #видаляємо старий номер
            self.phones.insert(0, Phone(new_phone)) #додаємо новий номер
        else:
            raise ValueError(f"Phone number {old_phone} not found.")

    def find_phone(self, phone):
        """Знаходить номер телефону в записі"""
        normalized = normalize_phone(phone)
        for p in self.phones: 
            if p.phone == normalized: #перевіряємо чи номер телефону є нормалізованим
                return str(p)
        return "Phone not found" 

    def add_email(self, email):
        """Додає email до запису"""
        if isinstance(email, str): #перевіряємо чи email є рядком
            email = Email(email) 
        self.emails.append(email) #додаємо email

    def remove_email(self, email):
        """Видаляє email з запису"""
        self.emails = [e for e in self.emails if e.email != email] #видаляємо email

    def edit_email(self, old_email, new_email):
        """Редагує email"""
        self.remove_email(old_email) #видаляємо старий email
        self.add_email(new_email) #додаємо новий email
    
    def find_email(self, email):
        """Знаходить email в записі"""
        for e in self.emails:
            if e.email == email: #перевіряємо чи email є в записі
                return str(e)
        return "Email not found"
    
    def add_address(self, city: str, street: str, house: str):
        """Додає адресу до запису"""
        self.address = Address(city, street, house) #додаємо адресу

    # def change_address(self, city: str, street: str, house: str):
    #     """Змінює адресу контакту"""
    #     if self.address:  #перевіряємо, чи існує адреса
    #         self.address = Address(city, street, house)  #оновлюємо адресу
    #     else:
    #         print("Address does not exist. Please add one first.")

    # def get_address(self):
    #     """Отримує адресу контакту"""
    #     if self.address:
    #         return str(self.address)  #повертаємо рядок, якщо адреса є
    #     return "No address"  #повертаємо повідомлення, якщо адреса відсутня


    def add_birthday(self, birthday):
        """Додає дату народження до запису"""
        if isinstance(birthday, str):
            self.birthday = Birthday(birthday)  #перетворюємо строку в дату через Birthday
        elif isinstance(birthday, date):
            self.birthday = birthday  #якщо дата вже передана, просто зберігаємо
        else:
            raise ValueError("Invalid type. Expected a string or a date object.")

    def __str__(self):
        """Повертає рядкове представлення запису"""
        phones_str = "; ".join(str(p) for p in self.phones) if self.phones else "No phones"
        emails_str = "; ".join(str(e) for e in self.emails) if self.emails else "No emails"
        birthday_str = str(self.birthday) if self.birthday else "No birthday"
        # address_str = str(self.address) if self.address else "No address for this user"

        if self.notes and self.notes.data:
            notes_list = [str(note) for note in self.notes.data.values()]
            notes_str = "\n    - " + "\n    - ".join(notes_list)
        else:
            notes_str = "No notes for this user"
        return f"Contact name: {self.name}, phones: {phones_str}, address:, emails: {emails_str}, birthday: {birthday_str}, notes: {notes_str}"

class AddressBook(UserDict):
    """Клас для збереження контактів"""
    def add_record(self, record):
        if not isinstance(record, Record): #перевіряємо чи запис є екземпляром класу Record
            raise ValueError("Record must be an instance of Record class.")
        self.data[str(record.name)] = record #додаємо запис до контактної книги

    def remove_record(self, name):
        """Видаляє запис з адресної книги"""
        if name in self.data: #перевіряємо чи запис існує
            del self.data[name] #видаляємо запис
        else:
            raise KeyError(f"Contact with name {name} not found.")

    def find_record(self, name):
        """Знаходить запис за ім'ям"""
        for record_name, record in self.data.items():
            if record_name.lower() == name.lower():  # Порівняння з ігноруванням регістру
                return record
        return None

    def __str__(self):
        """Повертає рядкове представлення адресної книги"""
        return "\n".join(str(record) for record in self.data.values()) #повертаємо всі записи в контактній книзі
    
    def upcoming_birthdays(self):
        """Повертає список майбутніх днів народження"""
        return get_upcoming_birthdays(self.data.values())
    
    def birthdays_pack(self, days: int) -> dict:
        """Повертає дні народження в заданий період"""
        return all_birthdays(self.data.values(), days)
    
# створення нової адресної книги
# book = AddressBook()

# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.add_email("jhon111@mail.com")
# john_record.add_birthday("1990-04-05")  # додаємо дату народження після створення

# додавання запису John до адресної книги
# book.add_record(john_record)

# # створення та додавання нового запису для Jane без дати народження
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# jane_record.add_email("jane111@mail.com")
# jane_record.add_birthday("1985-03-10")  # додаємо дату народження після створення
# book.add_record(jane_record)

# alica_record = Record("Alice")
# alica_record.add_phone("0963332211")
# alica_record.add_phone("0662221133")
# alica_record.add_email("alice@gmail.com")
# alica_record.add_birthday("1992-04-04")  # додаємо дату народження після створення
# book.add_record(alica_record)

# виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# виведення списку майбутніх днів народження
# upcoming_birthdays = book.upcoming_birthdays()
# print("List of greetings this week:", upcoming_birthdays)