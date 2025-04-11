from rich.console import Console
from rich.table import Table


def show_commands():
    console = Console()

    # Створення таблиці
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Command", style="dim", width=20)
    table.add_column("Description", justify="left")

    # Додавання команд до таблиці
    table.add_row("add", "Add new contact or information")
    table.add_row("change-phone", "Change phone number for contact")
    table.add_row("show-phones", "Show all phone numbers")
    table.add_row("all", "Show all contacts")
    table.add_row("remove", "Remove contact")
    table.add_row("add-address", "Add address for contact")
    table.add_row("show-address", "Show address for contact")
    table.add_row("change-address", "Change address for contact")
    table.add_row("show-contact", "Show contact information")
    table.add_row("add-birthday", "Add birthday for contact")
    table.add_row("show-birthday", "Show birthday for a contact")
    table.add_row("birthdays", "Show all upcoming birthdays")
    table.add_row("all-birthdays", "Show all birthdays")
    table.add_row("add-email", "Add email for contact")
    table.add_row("show-email", "Show email for contact")
    table.add_row("change-email", "Change email for contact")
    table.add_row("add-note", "Add note for contact")
    table.add_row("show-note", "Show notes for contact")
    table.add_row("change-note", "Change note for contact")
    table.add_row("remove-note", "Remove note for contact")
    table.add_row("hello", "Say hello")
    table.add_row("close", "Close the assistant bot")
    table.add_row("exit", "Exit the assistant bot")

    # # Виведення таблиці на екран
    console.print(table)

# Викликаємо функцію
#show_commands()
