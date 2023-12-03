x, y = map(int, input().split())
a, b = round(1 / x, 2), round(1 / y, 2)
s = ''
n = 0.01
num = 0

while 1:
    i = round(n * 100)
    if i % x == 0 and i % y == 0: s += '3'; num += 2
    elif i % x == 0: s += '2'; num += 1
    elif i % y == 0: s += '1'; num += 1
    n = round(n + 0.01, 2)

    if num == x + y: break

print(s[:num])
