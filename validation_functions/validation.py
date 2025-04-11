import re

def validate_name(name):
    """Перевіряє, чи ім'я містить лише літери та пробіли."""
    return bool(re.fullmatch(r"[A-Za-zА-Яа-яЁёІіЇїЄє ]+", name))

def validate_phone(phone):
    """Перевіряє, чи телефон складається лише з цифр і містить від 10 до 15 символів."""
    return bool(re.fullmatch(r"\d{10,15}", phone))

def name_validation(func):
    """Декоратор для перевірки імені."""
    def wrapper(*args, **kwargs):
        # Отримуємо ім'я з args
        name = args[0] if args else kwargs.get('name')
        
        # Перевірка чи name є рядком
        if not isinstance(name, str):
            return "Error: Name must be a string."
        
        return func(*args, **kwargs)
    return wrapper

def phone_validation(func):
    """Декоратор для перевірки телефону."""
    def wrapper(name, phone, *args, **kwargs):
        if not phone:
            return "Error: No phone number provided."
        if not validate_phone(phone):
            return "Error: Invalid phone number. It must be a number with 10 to 15 digits."
        return func(name, phone, *args, **kwargs)
    return wrapper

def input_error(func):
    """Декоратор для обробки помилок вводу."""
    def inner(*args, **kwargs):
        try:
            if func.__name__ in ['add_contact', 'change_contact']:
                name, phone = args[0], args[1]
                if not validate_name(name):
                    return "Error: Invalid name. Name must contain only letters and spaces."
                if not validate_phone(phone):
                    return "Error: Invalid phone number. It must be a number with 10 to 15 digits."
            result = func(*args, **kwargs)
            if result is None:
                return "Error: Something went wrong, no data returned."
            return result
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    return inner