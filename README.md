# Your Personal Assistant - Address Book

Your reliable assistant for managing contacts, addresses, birthdays, emails, and notes. Find the information you need quickly, add new contacts, and edit existing ones easily!

## Getting Started

### 1. Installation

If you are using Git, clone the repository:

`git clone https://github.com/alex-miami-petrov/gemini_3.0.git`
`cd gemini_3.0`

Install the necessary libraries:

`pip install prompt-toolkit rich urllib3`

### 2. Run the Bot

Run the bot:

`python main.py`

You will see a list of available commands.

### 3. How to Use the Bot

Commands:

## hello: Greeting.

## add <name> <phone number>: Add a contact.

Example: `add John +380501234567`

## change-phone <name> <new_phone_number>: Change a contact's phone number.

Example: `change-phone John +380679876543`

## show-contact <name>: View contact information.

Example: `show-contact John`

## remove <name>: Remove a contact.

Example: `remove John`

## show-phones <name>: View contact's phone numbers.

Example: `show-phones John`

## all: View all contacts.

## add-address <name> <city>, <street>, <house>: Add an address.

Example: `add-address John Kyiv, Khreshchatyk, 1`

## show-address <name>: View contact's address.

Example: `show-address John`

## change-address <name> <city>, <street>, <house>: Change an address.

Example: `change-address John Lviv, Sichovykh Striltsiv, 5`

## add-birthday <name> <year-month-day>: Add a birthday.

Example: `add-birthday John 1990-05-15`

## show-birthday <name>: View contact's birthday.

Example: `show-birthday John`

## birthdays: View upcoming birthdays.

## all-birthdays <number_of_days>: View birthdays within a period.

Example: `all-birthdays 7`

## add-email <name> <email>: Add an email.

Example: `add-email John john@example.com`

## show-email <name>: View contact's email.

Example: `show-email John`

## change-email <name> <new_email>: Change an email.

Example: `change-email John new_john@example.com`

## add-note <name> <title> <note_text>: Add a note.

Example: `add-note John Meeting notes Discuss project details.`

## show-note <name>: View contact's note.

Example: `show-note John`

## change-note <name> <title> <new_note_text>: Change a note.

Example: `change-note John Meeting notes Discuss new project details.`

## remove-note <name> <title>: Remove a note.

Example: `remove-note John Meeting notes`

## close or exit: Exit the bot.

### Additional Information

Data is stored in `addressbook.pkl`.

Use `Tab` for command autocompletion and arrow keys for command history.

For note tags, enter `y` after adding a note, then enter tags separated by commas.

### Data Validation

Name: Letters and spaces.

Phone: 10-15 digits, format `+38XXXXXXXXXXXXX`.

Email: Contains `@`.

Birthday: `YYYY-MM-DD`.

Address: "City, Street, House".

Notes: Any text, tags separated by commas.

Incorrect data will result in an error message.

#### Authors

"Legacy" Team:

alex-miami-petrov (TL) - [https://github.com/alex-miami-petrov/gemini_3.0](https://github.com/alex-miami-petrov/gemini_3.0)

DevDS7 - [https://github.com/DevDS7](https://github.com/DevDS7)

Mshukaliuk - [https://github.com/Mshukaliuk](https://github.com/Mshukaliuk)

Git-V1 - [https://github.com/Git-V1](https://github.com/Git-V1)
