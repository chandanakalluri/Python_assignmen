from Python_assignmen.src.assignment7.util import find_day
month, day, year = map(int, input().split())
print(find_day(month, day, year))