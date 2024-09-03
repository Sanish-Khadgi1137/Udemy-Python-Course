# import datetime

# #tap into datetime model and then datetime class
# #modeule
# datetime.datetime
#          #class

#confusing so 
#or
import datetime as dt

dat=dt.datetime.now()

print(dat)
print(type(dat))

year1 = dat.year

print(year1)

if year1 == 2024:
    print("twenty twenty four")


week_day = dat.weekday()#acc list start from 0(monday) if gives 2(wednesday) then is 3rd(wednesday) day of week
print(week_day)

birthday_date = dt.datetime(year=1997, month=11, day=18, hour=3, minute=1, microsecond=28)
print(birthday_date)