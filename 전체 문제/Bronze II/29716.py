j, n = map(int, input().split())
a = 0

for _ in range(n):
    i, s = input(), 0
    for c in i:
        if c.isupper(): s += 4
        if c.islower() or c.isdigit(): s += 2
        if c == ' ': s += 1
    if s <= j: a += 1

print(a)
