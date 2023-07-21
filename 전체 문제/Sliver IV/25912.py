l, n = set(), 0

for _ in range(int(input())):
    mg = input()
    if mg == 'ENTER': l.clear()
    else:
        if mg not in l:
            l.add(mg)
            n += 1
print(n)
