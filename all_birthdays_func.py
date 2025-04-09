from datetime import datetime, timedelta

def all_birthdays(records, number_of_days):
    """
    Повертає словник з іменами та днями народження, які припадають на наступні `number_of_days` днів (ігноруючи рік).
    """
    today = datetime.today()
    upcoming_dates = set(
        (today + timedelta(days=i)).strftime("%m-%d")
        for i in range(number_of_days + 1)
    )

    result = {}
    for record in records:
        if record.birthday:
            try:
                birthday_mmdd = record.birthday.date.strftime("%m-%d")
                if birthday_mmdd in upcoming_dates:
                    result[str(record.name)] = record.birthday
            except Exception as e:
                print(f"Error parsing birthday for {record.name}: {e}")

    return result
