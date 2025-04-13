# 🤖 Your Personal Assistant - LEGACY BOT 1.0

Your reliable assistant for managing contacts, addresses, birthdays, emails, and notes. Quickly find information, add new entries, and edit existing ones!

---

## ✨ Features

- **Contacts:** Add, edit, view, and remove contacts with phone numbers, addresses, emails, and birthdays.
- **Notes:** Save notes with tags for easy organization.
- **Data Management:** Change and view data by name.
- **Interactive Interface:** Enjoy interactive command hints during input.
- **Data Persistence:** Save data to `addressbook.pkl` file.
- **Birthday Reminders:** Search for upcoming birthdays.

---

### 1. Installation

If you are using Git, clone the repository:

`git clone https://github.com/alex-miami-petrov/legacy.git`

`cd gemini_3.0`

Install the necessary libraries:

`pip install prompt-toolkit rich urllib3`

### 2. Run the Bot

`python main.py`

You will see a list of available commands.

### 3. How to Use the Bot

## ️ Commands

### General Commands

- `hello` — Greeting
- `all` — View all contacts
- `close` / `exit` — Exit the bot
- `help` - Show commands

### Contact Commands

- `add <name> <phone number>`
  - Example: `add John +380501234567`
- `change-phone <name> <new_phone>`
  - Example: `change-phone John +380679876543`
- `show-contact <name>` — Show full information
- `show-phones <name>` — Show phone numbers
- `remove <name>` — Remove contact

### Address Commands

- `add-address <name> <city>, <street>, <house>`
  - Example: `add-address John Kyiv, Khreshchatyk, 1`
- `change-address <name> <city>, <street>, <house>`
  - Example: `change-address John Lviv, Sichovykh Striltsiv, 5`
- `show-address <name>` — Show address

### Birthday Commands

- `add-birthday <name> <YYYY-MM-DD>`
  - Example: `add-birthday John 1990-05-15`
- `show-birthday <name>` — Show birthday
- `birthdays` — Show upcoming birthdays
- `all-birthdays <days>` — Show birthdays for the specified period
  - Example: `all-birthdays 7`

### Email Commands

- `add-email <name> <email>`
  - Example: `add-email John john@example.com`
- `show-email <name>` — Show email
- `change-email <name> <new_email>`
  - Example: `change-email John new_john@example.com`

### Note Commands

- `add-note <name> <title> <note_text>`
  - Example: `add-note John Meeting Discuss project details.`
- `show-note <name>` — Show all notes
- `change-note <name> <title> <new_note_text>`
  - Example: `change-note John Meeting Update agenda.`
- `remove-note <name> <title>` — Remove note

**Note:** After adding a note, the bot will ask if you want to add tags — press `y` and enter tags separated by commas.

### Additional Information

Data is stored in `addressbook.pkl`.

To select a command from the list, press `↑ / ↓`, then `→` to autocomplete.

### Data Validation

Name: Letters and spaces.

Phone: 10-15 digits, format `+38XXXXXXXXXXXXX`.

Email: Contains `@`.

Birthday: `YYYY-MM-DD`.

Address: "City, Street, House".

Incorrect data will result in an error message.

#### Authors

"Legacy" Team:

alex-miami-petrov (TL) - [https://github.com/alex-miami-petrov/legacy]

DevDS7 - [https://github.com/DevDS7]

Mshukaliuk - [https://github.com/Mshukaliuk]

Git-V1 - [https://github.com/Git-V1]

##### Enjoy your personal assistant! 🎉
