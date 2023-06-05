from collections import deque

q = deque([i + 1 for i in range(int(input()))])
l = []

while len(q) > 1:
    l.append(q.popleft())
    q.append(q.popleft())
l.append(q[0])

print(*l)
