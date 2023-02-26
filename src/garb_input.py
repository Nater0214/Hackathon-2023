# garb_input.py
# For deciphering the garbage input


# Imports
import datetime


# Definitions
def decipher(txt: str) -> dict:
    """Decipher a garbage input into its parts and return"""
    
    # Convert input to all lower
    txt = txt.lower()
    txt = txt.split(' ')
    
    # Find date
    
    # Look for a month
    for month in ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"):
        try:
            if (month_ind := txt.index(month)) >= 0:
                break
        except ValueError:
            pass
        
        try:
            if (month_ind := txt.index(month[:3])) >= 0:
                break
        except ValueError:
            pass
    
    else:
        month = None
    
    # Look for date if there is a month
    if month:        
        for day in range(1, 32):
            try:
                if (date_ind := txt.index(str(day), month_ind)):
                    break
            except ValueError:
                continue
        
        else:
            day = None
        
        
        if day:
            date = datetime.datetime.strptime(f"{month} {day} {datetime.date.today().year}", "%B %d %Y")
            date = datetime.date(date.year, date.month, date.day)
    
    name = ' '.join(txt[:month_ind])
    name = name.capitalize()
    
    return {
        "name": name,
        "date": date
    }