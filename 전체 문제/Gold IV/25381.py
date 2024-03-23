from collections import deque as d
import sys

s = sys.stdin.readline().strip()
a, b = d(), d()
ans = 0

for i in range(len(s)):
  q = s[i]
  if q == 'A': a.append(i)
  elif q == 'B': b.append(i)
  elif b: b.popleft(); ans += 1

for i in a:
  while b and b[0] < i: b.popleft()
  if b: ans += 1; b.popleft()

print(ans)
