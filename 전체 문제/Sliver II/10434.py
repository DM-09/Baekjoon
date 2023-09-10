def SOE(MAX, MIN=1):
    box, l = [], [i + 1 for i in range(MAX)]

    for i in range(MAX):
        c = l[i]
        if c != 1 and c != 0:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = 0
            if c >= MIN: box.append(c)
    return box

def isHappy(n):
    l = []
    for _ in range(20):
        if n == 1: return 1
        if n in l: return 0

        s, a = str(n), 0
        for i in s: a += int(i) ** 2
        n = a
    return 0

b = SOE(10000)

for _ in range(int(input())):
    t, n = map(int, input().split())
    a = 'NO'
    if n in b:
        if isHappy(n): a = 'YES'

    print(t, n, a)
