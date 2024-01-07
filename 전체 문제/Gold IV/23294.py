from collections import deque

page = {}

n, q, c = map(int, input().split())

num = 1
for i in list(map(int, input().split())):
    page[num] = i
    num += 1

B = deque()
F = deque()
A = 0

cache = 0

for _ in range(q):
    cmd = input().split()
    a = cmd[0]

    if a == 'B':
        if not B: continue
        F.appendleft(A)
        A = B.pop()
    elif a == 'F':
        if not F: continue
        B.append(A)
        A = F.popleft()
    elif a == 'A':
        if A != 0: B.append(A)
        b = int(cmd[1])
        for i in F: cache -= page[i]
        F.clear()
        cache += page[b]
        A = b
        while cache > c: cache -= page[B.popleft()]
    elif a == 'C':
        pre, new = '', deque()
        for i in B:
            if i == pre: cache -= page[i]
            else: new.append(i)
            pre = i
        B = new

print(A)
if B: print(*reversed(B))
else: print(-1)
if F: print(*F)
else: print(-1)
