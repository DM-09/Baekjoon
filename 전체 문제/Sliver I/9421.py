def snum(n):
    r = []
    while 1:
        s = str(n)
        if s == '1': return 1
        new = 0
        for i in s: new += int(i) ** 2
        n = new
        if n in r: return 0
        r.append(new)

def SOE(MAX, MIN=1):
    box, l = [], [i + 1 for i in range(MAX)]

    for i in range(MAX):
        c = l[i]
        if c != 1 and c != 0:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = 0
            if c >= MIN: box.append(c)
    return box

n = int(input())
box = SOE(n)

for i in box:
    if snum(i): print(i)
