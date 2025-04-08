import re  # Додаємо для перевірки регулярних виразів

def validate_name(name):
    """Перевіряє, чи ім'я містить лише літери та пробіли."""
    return bool(re.fullmatch(r"[A-Za-zА-Яа-яЁёІіЇїЄє ]+", name))

def validate_phone(phone):
    """Перевіряє, чи телефон складається лише з цифр і містить від 10 до 15 символів."""
    return bool(re.fullmatch(r"\d{10,15}", phone))

def name_validation(func):
    """Декоратор для перевірки імені."""
    def wrapper(*args, **kwargs):
        if not args or not isinstance(args[0], list) or len(args[0]) == 0:
            return "Error: No name provided."
        name = args[0][0]  # беремо перший елемент зі списку аргументів
        if not validate_name(name):
            return "Error: Invalid name. Name must contain only letters and spaces."
        return func(*args, **kwargs)
    return wrapper

def phone_validation(func):
    """Декоратор для перевірки телефону."""
    def wrapper(*args, **kwargs):
        if not args or not isinstance(args[0], list) or len(args[0]) < 2:
            return "Error: No phone number provided."
        phone = args[0][1]  # беремо другий елемент зі списку аргументів
        if not validate_phone(phone):
            return "Error: Invalid phone number. It must be a number with 10 to 15 digits."
        return func(*args, **kwargs)
    return wrapper

def input_error(func):
    """Декоратор для обробки помилок введення користувача та перевірки даних."""
    def inner(*args, **kwargs):
        try:
            # перевірка валідності даних в залежності від функції
            if func.__name__ in ['add_contact', 'change_contact']:
                name, phone = args[0]  # отримуємо ім'я та телефон
                if not validate_name(name):
                    return "Error: Invalid name. Name must contain only letters and spaces."
                if not validate_phone(phone):
                    return "Error: Invalid phone number. It must be a number with 10 to 15 digits."
            result = func(*args, **kwargs)
            if result is None:  # додаємо перевірку на None
                return "Error: Something went wrong, no data returned."
            return result
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    return inner