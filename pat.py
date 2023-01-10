import calendar as cal
def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    elif 1700 <= year <= 1917 and year % 4 == 0 :
        return f"12.09.{year}"
#To use this method you must import calendar module.
    elif cal.isleap(year) == True: 
        return f"12.09.{year}"        
    else:
        return f"13.09.{year}"