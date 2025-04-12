from datetime import datetime, timedelta

def get_upcoming_birthdays(users) -> list:
    current_date = datetime.today().date()  
    next_week = current_date + timedelta(days=7)  
    upcoming_birthdays = []  
    
    for user in users:  
        if not user.birthday:  
            continue  
        
        birthday_date = user.birthday.date.replace(year=current_date.year)  
        
        if birthday_date < current_date:
            birthday_date = birthday_date.replace(year=current_date.year + 1)
        
        
        if current_date <= birthday_date <= next_week:
            if birthday_date.weekday() in [5, 6]:  
                congratulation_date = birthday_date + timedelta(days=(7 - birthday_date.weekday()))  
            else:
                congratulation_date = birthday_date

            
            upcoming_birthdays.append({
                "name": user.name.name,  
                "congratulation_date": congratulation_date.strftime("%Y-%m-%d") 
            })

    return upcoming_birthdays