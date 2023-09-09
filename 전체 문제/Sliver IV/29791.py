n, m = map(int, input().split())
a = list(set(map(int, input().split())))
o = list(set(map(int, input().split())))

aa, oo = 1, 1
ask, osk = 0, 0

a.sort(); o.sort()

for i in range(max(n, m) - 1):
    c1, c2 = 0, 0
    n1, n2 = 0, 0

    try: c1 = a[i]
    except: pass

    try: n1 = a[i + 1]
    except: pass

    try: c2 = o[i]
    except: pass

    try: n2 = o[i + 1]
    except: pass

    if n1 - ask >= 100: aa += 1; ask = n1
    if n2 - osk >= 360: oo += 1; osk = n2

print(aa, oo)
