d = list(input().split())
money = 0

if d[0] == d[1] == d[2]:
    money = 10000 + int(d[0]) * 1000
elif d[0] == d[1] or d[1] == d[2] or d[0] == d[2]:
    for i in range(6):
        if d.count(str(i + 1)) == 2:
            index = d.index(str(i + 1))
            money = 1000 + 100 * int(d[index])
            break
else:
    money = int(max(d)) * 100

print(money)
