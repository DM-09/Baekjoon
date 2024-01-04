import sys
input = sys.stdin.readline

def IP2Int(ip : str):
    new = ''
    for i in ip.split('.'): new += ('0' * (3 - len(i))) + i
    return int(new)

for _ in range(int(input())):
    d = {}
    ips = []

    for _ in range(int(input())):
        inp = input().split()
        name = inp[0]

        if len(inp[1:]) == 1: d[inp[1]] = name
        else: ips.append([IP2Int(inp[1]), IP2Int(inp[2]), name])

    for _ in range(int(input())):
        inp = input().split()
        l = []

        for i in inp:
            cur = i.replace('.', '')
            if not cur.isdigit():
                l.append(i)
                continue

            if d.get(i, 0): l.append(d[i]); continue

            for start, end, name in ips:
                if start <= IP2Int(i) <= end: l.append(name); break
            else: l.append(i)

        print(' '.join(l))
