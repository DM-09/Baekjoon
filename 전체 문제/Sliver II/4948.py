def SOE(MAX, MIN=1):
    box, l, s = set(), [i + 1 for i in range(MAX)], 0

    for i in range(len(l)):
        c = l[i]
        if c != 1 and c != -1:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = -1
            if c >= MIN: box.add(c)
    return list(box)

while 1:
    n = int(input())
    if n == 0: break
    print(len(SOE(n * 2, n + 1)))
