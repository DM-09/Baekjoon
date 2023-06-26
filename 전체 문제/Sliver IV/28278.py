import sys
l = []

input = sys.stdin.readline

for _ in range(int(input())):
    c, x = input().split(), 0
    if c[0] == '1': x = int(c[1])
    c = int(c[0])

    if c == 1: l.append(x)
    if c == 2: print(l.pop() if len(l) != 0 else -1)
    if c == 3: print(len(l))
    if c == 4: print(1 if len(l) == 0 else 0)
    if c == 5: print(l[-1] if len(l) != 0 else -1)
