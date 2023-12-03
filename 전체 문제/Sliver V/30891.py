import math

n, r = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

num = 0
a = []

for X in range(-100, 101):
    for Y in range(-100, 100):
        for x, y in l:
            if math.sqrt((X - x) ** 2 + (Y - y) ** 2) <= r:
                num += 1
        a.append([num, [X, Y]])
        num = 0

a.sort(key=lambda x: -x[0])
print(*a[0][1])
