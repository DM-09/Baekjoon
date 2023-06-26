import sys
from collections import deque

dq = deque()
input = sys.stdin.readline

for _ in range(int(input())):
    c = input()
    x = 0
    if c[0] in ['1', '2']: x, c = int(c.split()[1]), int(c.split()[0])
    c = int(c)

    if c == 1: dq.appendleft(x)
    if c == 2: dq.append(x)
    if c == 3: print(dq.popleft() if len(dq) != 0 else -1)
    if c == 4: print(dq.pop() if len(dq) != 0 else -1)
    if c == 5: print(len(dq))
    if c == 6: print(1 if len(dq) == 0 else 0)
    if c == 7: print(dq[0] if len(dq) != 0 else -1)
    if c == 8: print(dq[-1] if len(dq) != 0 else -1)
