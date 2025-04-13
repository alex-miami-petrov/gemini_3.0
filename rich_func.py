# from rich.console import Console
# from rich.table import Table


# def show_commands():
#     console = Console()

#     table = Table(show_header=True, header_style="bold magenta")
#     table.add_column("Command", style="dim", width=20)
#     table.add_column("Description", justify="left")

    
#     table.add_row("add", "Add new contact or information")
#     table.add_row("change-phone", "Change phone number for contact")
#     table.add_row("show-phones", "Show all phone numbers")
#     table.add_row("all", "Show all contacts")
#     table.add_row("remove", "Remove contact")
#     table.add_row("add-address", "Add address for contact")
#     table.add_row("show-address", "Show address for contact")
#     table.add_row("change-address", "Change address for contact")
#     table.add_row("show-contact", "Show contact information")
#     table.add_row("add-birthday", "Add birthday for contact")
#     table.add_row("show-birthday", "Show birthday for a contact")
#     table.add_row("birthdays", "Show all upcoming birthdays")
#     table.add_row("all-birthdays", "Show all birthdays")
#     table.add_row("add-email", "Add email for contact")
#     table.add_row("show-email", "Show email for contact")
#     table.add_row("change-email", "Change email for contact")
#     table.add_row("add-note", "Add note for contact")
#     table.add_row("show-note", "Show notes for contact")
#     table.add_row("change-note", "Change note for contact")
#     table.add_row("remove-note", "Remove note for contact")
#     table.add_row("hello", "Say hello")
#     table.add_row("close", "Close the assistant bot")
#     table.add_row("exit", "Exit the assistant bot")

    
#     console.print(table)

from rich.console import Console
from rich.table import Table


def show_commands():
    console = Console()

    console.print("[bold bright_cyan]=== LEGACY BOT 1.0 ===[/bold bright_cyan]", style="bold bright_cyan", justify="center", width=130)

    table = Table(show_header=True, header_style="bold magenta", show_lines=True)

    table.add_column("Command", style="dim", width=20)
    table.add_column("Description", justify="left")
    table.add_column("Example", justify="left")

    table.add_row("[green]add[/green]", "Add new contact with phone number", "[bold green]add[/bold green] <name> <phone number> (required 10 digits)")
    table.add_row("[green]change-phone[/green]", "Change phone number for contact", "[bold green]change-phone[/bold green] <name> <old phone number> <new phone number>")
    table.add_row("[green]show-phones[/green]", "Show all phone numbers for contact", "[bold green]show-phones[/bold green] <name>")
    table.add_row("[green]all[/green]", "Show all contacts", "[bold green]all[/bold green]")
    table.add_row("[green]remove[/green]", "Remove contact", "[bold green]remove[/bold green] <name>")
    table.add_row("[green]add-address[/green]", "Add address for contact", "[bold green]add-address[/bold green] <name> <city> <street> <house>")
    table.add_row("[green]show-address[/green]", "Show address for contact", "[bold green]show-address[/bold green] <name>")
    table.add_row("[green]change-address[/green]", "Change address for contact", "[bold green]change-address[/bold green] <name> <city> <street> <house>")
    table.add_row("[green]show-contact[/green]", "Show contact information", "[bold green]show-contact[/bold green] <name>")
    table.add_row("[green]add-birthday[/green]", "Add birthday for contact", "[bold green]add-birthday[/bold green] <name> <birthday> (required format YYYY-MM-DD)")
    table.add_row("[green]show-birthday[/green]", "Show birthday for a contact", "[bold green]show-birthday[/bold green] <name>")
    table.add_row("[green]birthdays[/green]", "Show all congratulations dates for birthdays", "[bold green]birthdays[/bold green]")
    table.add_row("[green]all-birthdays[/green]", "Show all birthdays in specified days", "[bold green]all-birthdays[/bold green] <number of days>")
    table.add_row("[green]add-email[/green]", "Add email for contact", "[bold green]add-email[/bold green] <name> <email>")
    table.add_row("[green]show-email[/green]", "Show email for contact", "[bold green]show-email[/bold green] <name>")
    table.add_row("[green]change-email[/green]", "Change email for contact", "[bold green]change-email[/bold green] <name> <old email> <new email>")
    table.add_row("[green]add-note[/green]", "Add note for contact", "[bold green]add-note[/bold green] <name> <title> <note>")
    table.add_row("[green]show-note[/green]", "Show notes for contact", "[bold green]show-note[/bold green] <name>")
    table.add_row("[green]change-note[/green]", "Change note for contact", "[bold green]change-note[/bold green] <name> <title> <new note>")
    table.add_row("[green]remove-note[/green]", "Remove note for contact", "[bold green]remove-note[/bold green] <name> <title>")
    table.add_row("[green]hello[/green]", "Say hello", "[bold green]hello[/bold green]")
    table.add_row("[green]close[/green]", "Close the assistant bot", "[bold green]close[/bold green]")
    table.add_row("[green]exit[/green]", "Exit the assistant bot", "[bold green]exit[/bold green]")
    table.add_row("[green]help[/green]", "Show all commands", "[bold green]help[/bold green]")

    console.print(table)




