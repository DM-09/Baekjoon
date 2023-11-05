from datetime import datetime

def solve(stamp, due):
    if stamp[0] == '12' and due[0] == '1':
        due.append(int(stamp[2]) + 1)

    elif stamp[0] == '1' and due[0] == '12':
        due.append(int(stamp[2]) - 1)

    else: due.append(int(stamp[2]))

    s = datetime(int(stamp[2]), int(stamp[0]), int(stamp[1]))
    d = datetime(int(due[2]), int(due[0]), int(due[1]))

    diff = (d - s).days
    day_str = 'DAYS'

    if abs(diff) == 1: day_str = 'DAY'

    if diff == 0: print('SAME DAY')
    elif diff > 0 and diff < 8: print(f'{d.month}/{d.day}/{d.year} IS {diff} {day_str} AFTER')
    elif diff > -8 and diff < 0: print(f'{d.month}/{d.day}/{d.year} IS {diff * -1} {day_str} PRIOR')
    else: print('OUT OF RANGE')

for _ in range(int(input())):
    q = input().split()
    stamp = q[0].split('/')
    due = q[1].split('/')

    solve(stamp, due)
