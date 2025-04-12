import re

def normalize_phone(phone):
    pattern = r"[\\n\\t()/;,\-:!\s\.]+" 
    number = re.sub(pattern, "", phone) 
    
    if re.match(r"^\+38", number): 
        return number  
    elif re.match(r"^38", number): 
        return "+" + number  
    else:
        return "+38" + number 