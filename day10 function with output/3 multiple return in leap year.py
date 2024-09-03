def is_leap(year):
    """Check if the year 
    is a leap year"""
    #(Docstrings) say about user define function; the first line after the name of funtion with triple quotation
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def day_in_month(year, month):
   
    if month > 12 or month < 1:
        return "invalid input" #direct print out this message
    
    month_days= [31,28,31,30,31,30,31,31,30,31,30,31,30]

       #hovering on the function call show the Docstrings
    if is_leap(year) and month == 2: #funtion inside funtion
        return 29
    return month_days[month - 1] # no need of else here

year = int(input("enter a year: "))
month = int(input("enter a month: "))

day = day_in_month(year, month)

print(day)