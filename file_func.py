import pickle
from address_book import AddressBook

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            book = pickle.load(f)

            
            for name, record in book.data.items():  
                if isinstance(record.name, bytes):
                    record.name = record.name.decode('utf-8')  

                
                for i, phone in enumerate(record.phones):
                    if isinstance(phone, bytes):
                        record.phones[i] = phone.decode('utf-8')  

            return book
    except FileNotFoundError:
        return AddressBook()  
