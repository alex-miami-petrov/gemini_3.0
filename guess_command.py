from prompt_toolkit.completion import WordCompleter

commands_list = [
    "add", "change-phone", "remove", "add-birthday", "add-email",
    "change-email", "add-note", "change-note", "remove-note", "add-address",
    "change-address", "show-contact", "show-phones", "all", "show-address",
    "show-birthday", "birthdays", "all-birthdays", "hello", "close", "exit", "show-note"
]

def get_completer():
    """Функція для отримання об'єкта автозаповнення для команд"""
    return WordCompleter(commands_list, ignore_case=True)