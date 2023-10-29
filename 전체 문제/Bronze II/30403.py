upp, low = sorted(list('roygbiv')), sorted(list('ROYGBIV'))
up, lo = set(), set()
n = int(input())
s = input()

if n < 7: print('NO!')
else:
    for i in s:
        if i in "roygbiv": up.add(i)
        elif i in 'ROYGBIV': lo.add(i)

    up, lo = list(up), list(lo)
    up.sort()
    lo.sort()

    if up == upp and lo == low: print('YeS')
    elif up == upp: print('yes')
    elif lo == low: print('YES')
    else: print('NO!')
