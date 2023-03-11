import datetime

month, day = map(int, input().split())
weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

print(weekday[datetime.datetime(2007, month, day).weekday()])
