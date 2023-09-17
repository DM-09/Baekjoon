def SOE(MAX, MIN=1):
    box, l = [], [i + 1 for i in range(MAX)]

    for i in range(MAX):
        c = l[i]
        if c != 1 and c != 0:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = 0
            if c >= MIN: box.append(c)
    return box

a, b, d = map(int, input().split())
box = SOE(b, a)
n, d = 0, str(d)

for i in box:
    if str(i).find(d) != -1: n += 1

print(n)
