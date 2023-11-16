def SOE(MAX, MIN=1):
    box, l = [], [i + 1 for i in range(MAX)]

    for i in range(MAX):
        c = l[i]
        if c != 1 and c != 0:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = 0
            if c >= MIN: box.append(c)
    return box

box = SOE(1299709)

for _ in range(int(input())):
    k = int(input())

    if k in box: print(0)
    else:
        pre = end = 0

        for i in box:
            if i > k: end = i; break
            pre = i

        print(end - pre)

