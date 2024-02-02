from heapq import *
n = int(input())
q = []

for _ in range(n): heappush(q, int(input()))
if n == 1: print(0); exit(0)

p = 0
while 1:
  a, b = heappop(q), heappop(q)
  heappush(q, a+b)
  p += a+b
  if len(q) == 1: break

print(p)
