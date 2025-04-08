from collections import UserDict
from normalize import normalize_phone
from datetime import datetime, date
from birthdays_func import get_upcoming_birthdays

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
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = [] 
        self.emails = []
        self.birthday = birthday if birthday else None

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
        
        return f"Contact name: {self.name}, phones: {phones_str}, emails: {emails_str}, birthday: {birthday_str}"

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
        return self.data.get(name, None) #повертаємо запис за ім'ям

    def __str__(self):
        """Повертає рядкове представлення адресної книги"""
        return "\n".join(str(record) for record in self.data.values()) #повертаємо всі записи в контактній книзі
    
    def upcoming_birthdays(self):
        """Повертає список майбутніх днів народження"""
        return get_upcoming_birthdays(self.data.values())
    
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