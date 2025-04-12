import re

def validate_name(name):
    """Перевіряє, чи ім'я містить лише літери та пробіли."""
    return bool(re.fullmatch(r"[A-Za-zА-Яа-яЁёІіЇїЄє ]+", name))

def validate_phone(phone):
    """Перевіряє, чи телефон складається лише з цифр і містить від 10 до 15 символів."""
    if len(phone) < 10 or len(phone) > 15:
        return False
    return bool(re.fullmatch(r"\d{10,15}", phone))

def name_validation(func):
    def wrapper(args, book, *other, **kwargs):
        if not args or len(args) < 1 or not isinstance(args[0], str):
            return "Error: Name is missing or invalid."

        name = args[0]

        if not validate_name(name):
            return "Error: Invalid name. Only letters and spaces allowed."

        return func(args, book, *other, **kwargs)
    return wrapper

def phone_validation(func):
    def wrapper(args, book, *other, **kwargs):
        if len(args) < 2 or not isinstance(args[1], str):
            return "Error: Phone number is missing or invalid."

        phone = args[1]

        if not validate_phone(phone):
            return "Error: Invalid phone number. It must be a number with 10 to 15 digits."

        return func(args, book, *other, **kwargs)
    return wrapper

def input_error(func):
    """Декоратор для обробки помилок вводу."""
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                return "Error: Something went wrong, no data returned."
            return result
        except AttributeError as e:
            return f"AttributeError: {str(e)}. It seems that the 'address' attribute is missing in the Record object."
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    return inner