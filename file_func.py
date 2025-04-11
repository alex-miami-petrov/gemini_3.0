import pickle
from address_book import AddressBook

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            book = pickle.load(f)

            # Перевірка і перетворення байтів у рядки для кожного контакту
            for name, record in book.data.items():  # Тут використовуємо book.data, оскільки self.data містить записи
                if isinstance(record.name, bytes):
                    record.name = record.name.decode('utf-8')  # Перетворення на рядок

                # Перевіряємо телефони і перетворюємо, якщо вони у байтовому форматі
                for i, phone in enumerate(record.phones):
                    if isinstance(phone, bytes):
                        record.phones[i] = phone.decode('utf-8')  # Перетворення на рядок

            return book
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено
