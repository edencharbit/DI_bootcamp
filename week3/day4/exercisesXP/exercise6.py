# Exercise 6: Birthday and minutes


import datetime

def minutes_in_live(birth_date):

    format_birth_day = datetime.datetime.strptime(birth_date, '%d/%m/%Y')
    current_day = datetime.datetime.now()
    diff = current_day - format_birth_day
    total_sec = diff.total_seconds()
    total_min = int(total_sec/60)
    print(f"You have lived {total_min} minutes in your life")



minutes_in_live("30/07/1999")
