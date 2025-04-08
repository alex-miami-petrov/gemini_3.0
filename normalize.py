import re

def normalize_phone(phone):
    pattern = r"[\\n\\t()/;,\-:!\s\.]+" #створюємо шаблон не потрібних символів в номерах
    number = re.sub(pattern, "", phone) #видаляємо не потрібні символи
    
    if re.match(r"^\+38", number): #шукаємо +38 на початку
        return number  
    elif re.match(r"^38", number): #шукаємо 38 і додаємо + на початку
        return "+" + number  
    else:
        return "+38" + number #в усіх інших випадках додаємо +38