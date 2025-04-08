from datetime import datetime, timedelta

def get_upcoming_birthdays(users) -> dict:
    current_date = datetime.today().date()  # поточна дата
    next_week = current_date + timedelta(days=7)  # дата через 7 днів
    upcoming_birthdays = []  # список для майбутніх днів народження
    
    for user in users:  # працюємо з об'єктами класу Record
        birthday_date = user.birthday.date.replace(year=current_date.year)  # переведення на поточний рік
        # якщо день народження вже був у цьому році, переносимо на наступний
        if birthday_date < current_date:
            birthday_date = birthday_date.replace(year=current_date.year + 1)
        
        # якщо день народження припадає на вихідні, переносимо на понеділок
        if current_date <= birthday_date <= next_week:
            if birthday_date.weekday() in [5, 6]:  # перевірка на вихідні (субота, неділя)
                congratulation_date = birthday_date + timedelta(days=(7 - birthday_date.weekday()))  # переносимо на понеділок
            else:
                congratulation_date = birthday_date

            # додаємо в список
            upcoming_birthdays.append({
                "name": user.name.name,  # використовуючи атрибут name з класу Record
                "congratulation_date": congratulation_date.strftime("%Y-%m-%d")  # формат дати
            })

    return upcoming_birthdays