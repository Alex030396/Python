# DATES

from datetime import datetime as dt

now = dt.now()

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

print("--------------------------")
timestamp = now.timestamp()
print(timestamp)

year_2027 = dt(2027,1,1)
print(year_2027)

print("--------------------------")

def print_date (date):    
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.microsecond)
    print(date.timestamp())
    
print_date(now)
print("--------------------------")

from datetime import time
current_time = time(14,31,0)
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print("--------------------------")

from datetime import date
current_date = date(1996,3,3)
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date.today()
print(current_date)

print("--------------------------")

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date)

print("--------------------------")
diff = year_2027 - now
print(diff)
diff = year_2027.date() - current_date
print(diff)

print("--------------------------")
from datetime import timedelta
init_timedelta = timedelta(200,100,100, weeks=10)
end_timedelta = timedelta(300,100,100, weeks=13)
print(end_timedelta - init_timedelta)