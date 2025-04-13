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
        if not isinstance(name, str) or not name.replace(" ", "").isalpha(): 
            raise ValueError("Name must be a string containing only letters and spaces.") 
        self.name = name 

    def __str__(self):
        return self.name

class Phone(Field):
    """Клас для зберігання номера телефону"""
    def __init__(self, phone):
        if not isinstance(phone, str) or not phone.isdigit(): 
            raise ValueError("Phone number must be a string containing only digits.") 
        self.phone = normalize_phone(phone)  

    def __str__(self):
        return self.phone 

class Email(Field):
    """Клас для зберігання email"""
    def __init__(self, email):
        if not isinstance(email, str) or "@" not in email: 
            raise ValueError("Email must be a valid string containing '@'.")
        self.email = email 

    def __str__(self):
        return self.email
class Address(Field):
    """Клас для зберігання адреси"""
    def __init__(self, address: str = None):
        if not isinstance(address, str):
            raise ValueError("Add something to address.")
        self.address = address

    def __str__(self):
        return f"{self.address}"

    
class Notes(Field):
    """Клас для зберігання notes"""
    def __init__(self, title, notes, tag = None):
        if not isinstance(notes, str):
            raise ValueError("Add something to notes.")
        self.id = str(uuid4())
        self.title = title or "Untitled"
        self.notes = notes 
        self.tag = set(tag) if tag else set()


    def add_tag(self, tag):
        if not isinstance(tag, str): 
            raise ValueError("Tag must be a string.")
        self.tag.add(tag.lower()) 

    def remove_tag(self, tag):
        if tag in self.tag:
            self.tag.remove(tag.lower())

    def show_tags(self):
        if not self.tag:
            return "No tags"
        return ", ".join(tag for tag in self.tag)
    
    def remove_tag(self, tag):
        self.tag.discard(tag.lower())

    def change_tag(self, old_tag, new_tag):
        old, new = old_tag.lower(), new_tag.lower()
        if old in self.tag:
            self.tags.remove(old)
            self.tags.add(new)
    
    def __str__(self):
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
        self.data = {} 

    def add_note(self, notes):
        self.data[notes.id] = notes 

    def delete_note(self, note_id):
        return self.data.pop(note_id, None) is not None 
    
    def find_note(self, note_id):
        return self.data.get(note_id, None)


    def edit_note(self, title, new_note_text):
        """Редагує текст нотатки за її заголовком, залишаючи заголовок незмінним."""
        for note in self.data.values():
            if note.title == title:  
                note.notes = new_note_text  
                return True  
        return False  

    
    def show_notes(self):
        """Повертає всі нотатки у форматі рядка"""
        if not self.data:
            return "No notes available."
        return "; ".join(str(note) for note in self.data.values())
    
    # def __str__(self):
    #     return self.show_notes()


    # def __str__(self):
    #     if not self.data:
    #         return "No notes"
    #     return "\n".join(str(note) for note in self.data.values())


class Birthday(Field):
    """Клас для зберігання дати народження"""
    def __init__(self, birthday):
        if not isinstance(birthday, str): 
            raise ValueError("Birthday must be a string in the format 'YYYY-MM-DD'.")
        self.birthday = self._parse_date(birthday) 
        
    def _parse_date(self, birthday):
        """Парсить дату народження з рядка"""
        try:
            return datetime.strptime(birthday, "%Y-%m-%d").date() 
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        
    @property
    def date(self):
        """Властивість для доступу до дати народження"""
        return self.birthday

    def __str__(self):
        return self.birthday.strftime("%Y-%m-%d") 

class Record:
    """Клас для зберігання інформації про контакт"""
    def __init__(self, name, address=None, birthday=None, notes=None):
        self.name = Name(name)
        self.phones = [] 
        self.emails = []
        self.birthday = birthday if birthday else None
        self.notes = notes if isinstance(notes, BookForNotes) else BookForNotes()
        self.address = None

    def add_phone(self, phone):
        """Додає номер телефону до запису"""
        phone = Phone(phone) if isinstance(phone, str) else phone
        if phone.phone not in [p.phone for p in self.phones]:  
            self.phones.append(phone)
        else:
            raise ValueError(f"Phone {phone.phone} already exists.")

    def remove_phone(self, phone):
        """Видаляє номер телефону з запису"""
        normalized_phone = normalize_phone(phone)
        self.phones = [p for p in self.phones if p.phone != normalized_phone] 

    def edit_phone(self, old_phone: str, new_phone: str):
        """Редагує номер телефону"""
        if self.find_phone(old_phone):
            self.remove_phone(old_phone) 
            self.phones.insert(0, Phone(new_phone)) 
        else:
            raise ValueError(f"Phone number {old_phone} not found.")

    def find_phone(self, phone):
        """Знаходить номер телефону в записі"""
        normalized = normalize_phone(phone)
        for p in self.phones: 
            if p.phone == normalized: 
                return str(p)
        return "Phone not found" 

    def add_email(self, email):
        """Додає email до запису"""
        if isinstance(email, str): 
            email = Email(email) 
        self.emails.append(email) 

    def remove_email(self, email):
        """Видаляє email з запису"""
        self.emails = [e for e in self.emails if e.email != email] 

    def edit_email(self, old_email, new_email):
        """Редагує email"""
        self.remove_email(old_email) 
        self.add_email(new_email) 
    
    def find_email(self, email):
        """Знаходить email в записі"""
        for e in self.emails:
            if e.email == email: 
                return str(e)
        return "Email not found"
    
    def add_address(self, address: str):
        """Додає адресу до запису"""
        self.address = Address(address) 

    def change_address(self, address):
        """Змінює адресу контакту"""
        if self.address:  
            self.address = Address(address) 
        else:
            print("Address does not exist. Please add one first.")

    def get_address(self):
        """Отримує адресу контакту"""
        if self.address:
            return str(self.address)
        return "No address"  


    def add_birthday(self, birthday):
        """Додає дату народження до запису"""
        if isinstance(birthday, str):
            self.birthday = Birthday(birthday)
        elif isinstance(birthday, date):
            self.birthday = birthday
        else:
            raise ValueError("Invalid type. Expected a string or a date object.")

    def __str__(self):
        """Повертає рядкове представлення запису"""
        phones_str = "; ".join(str(p) for p in self.phones) if self.phones else "No phones"
        emails_str = "; ".join(str(e) for e in self.emails) if self.emails else "No emails"
        birthday_str = str(self.birthday) if self.birthday else "No birthday"
        
        if self.notes and self.notes.data:
            notes_list = [str(note) for note in self.notes.data.values()]
            notes_str = "\n" + "\n    - ".join(notes_list)
        else:
            notes_str = "No notes for this user"
        return f"Contact name: {self.name}, phones: {phones_str}, address: {self.address}, emails: {emails_str}, birthday: {birthday_str}, notes: {notes_str}"

class AddressBook(UserDict):
    """Клас для збереження контактів"""
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Record must be an instance of Record class.")
        self.data[str(record.name)] = record 

    def remove_record(self, name):
        """Видаляє запис з адресної книги"""
        if name in self.data: 
            del self.data[name] 
        else:
            raise KeyError(f"Contact with name {name} not found.")

    def find_record(self, name):
        """Знаходить запис за ім'ям"""
        for record_name, record in self.data.items():
            if record_name.lower() == name.lower(): 
                return record
        return None

    def __str__(self):
        """Повертає рядкове представлення адресної книги"""
        return "\n".join(str(record) for record in self.data.values()) 
    
    def upcoming_birthdays(self):
        """Повертає список майбутніх днів народження"""
        return get_upcoming_birthdays(self.data.values())
    
    def birthdays_pack(self, days: int) -> dict:
        """Повертає дні народження в заданий період"""
        return all_birthdays(self.data.values(), days)
    
