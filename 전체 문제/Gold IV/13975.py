from heapq import *

for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  heapify(l)
  a = 0
  while len(l) > 1:
    q, w = heappop(l), heappop(l)
    e = q + w
    a += e
    heappush(l, e)
  print(a)
