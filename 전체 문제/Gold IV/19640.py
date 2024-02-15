from heapq import *
import sys
from collections import *

input = sys.stdin.readline

n, m, k = map(int, input().split())
ans = 0
a = [deque() for _ in range(m)]

q = 0
for i in range(n):
  d, h = map(int, input().split())
  a[q].append([-d, -h, q, i])
  q += 1
  if q == m: q = 0

heapify(a)

while a:
  b = heappop(a)
  if not b: continue
  c = b.popleft(); ans += 1
  if b: heappush(a, b)
  if c[-1] == k: break

print(ans - 1)
