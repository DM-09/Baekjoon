months = {'January': 0, 'February': 31, 'March': 59, 'April': 90, 'May': 120, 'June': 151, 'July': 181, 'August': 212, 'September': 243, 'October': 273, 'November': 304, 'December': 334}

month, day, year, today_time = input().split()
year = int(year)
days_passed = months[month] + int(day[:2]) - 1

total_days = 365
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
  total_days = 366
  if not month in ['January', 'February']:
    days_passed += 1


H, M = today_time.split(':')
total_minute = int(H) * 60 + int(M)

ratio = total_minute / 1440
      
days_passed += ratio

print(days_passed / total_days * 100)
