n, m, k = map(int, input().split())
num = 0

for _ in range(n):
    l, s = [], ''
    for i in input():
        if i == '0': s += i
        else: l.append(s); s = ''

    l.append(s)

    for i in l:
        if len(i) >= k: num += 1 + len(i) - k

print(num)

