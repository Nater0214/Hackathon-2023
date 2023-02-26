# garb_input.py
# For deciphering the garbage input


# Imports
import calendar


# Definitions
def decipher(txt: str) -> dict:
    """Decipher a garbage input into its parts and return"""
    
    # Convert input to all lower
    txt = txt.lower()
    
    # Find date
    
    # Look for a month
    for month in ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"):
        if (month_ind := txt.find(month)) >= 0 or (month_ind := txt.find(month[0:3])) >= 0:
            break
    
    else:
        month = None
    
    # Look for date if there is a month
    if month:        
        for date in range(1, 32):
            if (date_ind := txt.find(str(date), month_ind)):
                break
        
        else:
            date = None
        
        # Look for year if there is a date
        if date:
            