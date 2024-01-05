from collections import deque

B = deque()
F = deque()
A = None

n, q = map(int, input().split())

for _ in range(q):
    cmd = input().split()
    c = cmd[0]

    if c == 'B':
        if len(B) == 0: continue
        F.appendleft(A)
        A = B.pop()
    elif c == 'F':
        if len(F) == 0: continue
        B.append(A)
        A = F.popleft()
    elif c == 'A':
        F.clear()
        if A: B.append(A)
        A = int(cmd[1])
    elif c == 'C':
        pre, new = 'X', deque()
        for i in B:
            if i != pre: new.append(i)
            pre = i
        B = new

print(A)
if len(B): print(*reversed(B))
else: print(-1)

if len(F): print(*F)
else: print(-1)
