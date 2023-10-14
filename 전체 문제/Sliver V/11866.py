from collections import deque

n, k = map(int, input().split())
q = deque()
l = []

for i in range(n): q.append(i + 1)

while q:
  q.rotate(-k + 1)
  l.append(q.popleft())

print('<' + ', '.join(map(str, l)) + '>')
