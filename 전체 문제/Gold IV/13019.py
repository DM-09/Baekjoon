from collections import *
a = deque(input())
b = deque(input())

ans = 0
da, db = defaultdict(int), defaultdict(int)
for i in range(len(a)): da[a[i]] += 1; db[b[i]] += 1

for i in da:
  if da[i] != db[i]: print(-1); exit()

for i in range(len(a)):
  if a[-1] == b[-1]: a.pop(); b.pop()
  else: a.rotate(); ans += 1

print(ans)
