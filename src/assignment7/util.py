import calendar


def find_day(month, day, year):
    weekday_index = calendar.weekday(year, month, day)
    weekday_name = calendar.day_name[weekday_index]
    return weekday_name.upper()



