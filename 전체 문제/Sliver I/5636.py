def SOE(MAX, MIN=1):
    box, l = [], [i + 1 for i in range(MAX)]

    for i in range(MAX):
        c = l[i]
        if c != 1 and c != 0:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = 0
            if c >= MIN: box.append(str(c))
    return box

pns = SOE(100000)


while 1:
    i = input()
    if i == '0': break

    a = [0]

    for r in pns:
        if int(r) > int(i): break
        if r in i: a.append(int(r))

    print(max(a))
