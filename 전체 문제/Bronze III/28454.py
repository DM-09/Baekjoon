from datetime import *

ty, tm, td = map(int, input().split('-'))
today = date(ty, tm, td)
l = []

c = 0

for _ in range(int(input())):
    yy, mm, dd = map(int, input().split('-'))
    l.append(date(yy, mm, dd))

for i in l:
    if (i - today).days >= 0: c += 1
print(c)
