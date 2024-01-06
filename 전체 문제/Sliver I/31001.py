from decimal import Decimal

n, m, q = map(int, input().split())
have = {}
group = {}
com = {}

for _ in range(n):
    g, h, p = input().split()
    g, p = int(g), int(p)

    have[h] = 0
    group[h] = g

    try: com[g][h] = p
    except: com[g] = {h : p}

for _ in range(q):
    cmd = input().split()
    c = cmd[0]

    if c == '1':
        A, B = cmd[1], int(cmd[2])
        money = com[group[A]][A] * B
        if m >= money:
            m -= money
            have[A] += B
    elif c == '2':
        A, B = cmd[1], int(cmd[2])
        S = have[A]
        if S == 0: continue
        if B >= S:
            m += com[group[A]][A] * S
            have[A] = 0
        elif S >= B:
            m += com[group[A]][A] * B
            have[A] -= B
    elif c == '3':
        A, C = cmd[1], int(cmd[2])
        com[group[A]][A] += C
    elif c == '4':
        D, C = int(cmd[1]), int(cmd[2])
        for i in com[D]: com[D][i] += C
    elif c == '5':
        D, E = int(cmd[1]), int(cmd[2])
        for i in com[D]:
            x = Decimal(str((100 + E) / 100)) * com[D][i]
            com[D][i] = int(x - (x % 10))
    elif c == '6': print(m)
    else:
        sev = m
        for i in have: sev += com[group[i]][i] * have[i]
        print(sev)
