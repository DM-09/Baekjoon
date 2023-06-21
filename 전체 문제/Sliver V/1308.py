from datetime import datetime

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

today = datetime(year=y1, month=m1, day=d1)
dday = datetime(year=y2, month=m2, day=d2)
y1000 = datetime(year=y1 + 1000, month=m1, day=d1)

t = today - dday

if t.days <= (today - y1000).days:
    print('gg')
else:
    print('D'+str(t.days))
