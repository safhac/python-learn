"""
For the years 1901 to 2000, count the total number of Sundays that fell on the first of a month.
"""
import datetime

count = 0

for y in range(1901, 2001):
    for m in range(1, 13):
        d = datetime.datetime(y, m, 1)

        if d.weekday() == 6:
            count += 1


print(f'the number of sundays {count}')