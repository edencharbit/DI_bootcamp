# Exercise 5: Amount of time left until January 1st


import datetime

def time_till_jan1st():
    current_date = datetime.datetime.now()
    next_year = current_date.year + 1
    new_year = datetime.datetime(next_year, 1, 1)
    diff = new_year-current_date
    days = diff.days
    print(f"The time left until January 1st is {days} days")


time_till_jan1st()