# WAP to find how many days, weeks and months remaining
# application of mathmatical operation and f-String 

age=input("Enter your current age: ")

age_as_int=int(age)

remaining_life = 90 - age_as_int

days_remaining =remaining_life *365
weeks_remaining = remaining_life * 52
months_remaining = remaining_life *12

print(f"You have {days_remaining} days or {weeks_remaining} weeks or {months_remaining} months")