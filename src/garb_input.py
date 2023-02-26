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
    date = None
    
    # Look for a month
    for month in ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"):
        try:
            if (date_ind := txt.index(month)) >= 0:
                break
        except ValueError:
            pass
        
        try:
            if (date_ind := txt.index(month[:3])) >= 0:
                break
        except ValueError:
            pass
    
    else:
        month = None
    
    # Look for date if there is a month
    if month:        
        for day in range(1, 32):
            try:
                if txt.index(str(day), date_ind):
                    break
            except ValueError:
                continue
        
        else:
            day = None
        
        
        if day:
            # Get date and day from string
            date = datetime.datetime.strptime(f"{month} {day}", "%B %d")
            
            # Get the date closest to today
            if abs((this_year_date := datetime.date(datetime.date.today().year, date.month, date.day)) - datetime.date.today()) < abs(((next_year_date := datetime.date(datetime.date.today().year + 1, date.month, date.day))) - datetime.date.today()):
                if abs((last_year_date := datetime.date(datetime.date.today().year - 1, date.month, date.day)) - datetime.date.today()) < abs(this_year_date - datetime.date.today()):
                    date = last_year_date
                else:
                    date = this_year_date
            else:
                date = next_year_date
    
    # Look for yesterday or today or tomorrow
    else:
        # Yesterday
        try:
            date_ind = txt.index("today")
            date = datetime.date.today() - datetime.timedelta(days = 1)
        except ValueError:
            pass
        
        # Today
        try:
            date_ind = txt.index("today")
            date = datetime.date.today()
        except ValueError:
            pass
        
        # Tomorrow
        try:
            date_ind = txt.index("tomorrow")
            date = datetime.date.today() + datetime.timedelta(days = 1)
        except ValueError:
            pass
    
    # Get name
    name = ' '.join([word.capitalize() for word in txt[:date_ind]])
    
    return {
        "name": name,
        "date": date
    }