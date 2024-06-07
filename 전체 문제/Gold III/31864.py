from sys import stdin
from math import gcd
from collections import *
from bisect import bisect_left, bisect_right

input = stdin.readline

n, m = map(int, input().split())
p = defaultdict(list)

def r(x, y):
  g = gcd(x, y)
  return (x // g, y // g)

for _ in range(n):
  x, y = map(int, input().split())
  p[r(x, y)].append([x, y])

for i in p: p[i].sort()

t = 0
for _ in range(m):
  x, y = map(int, input().split())
  a = r(x, y)
  
  bl = bisect_right(p.get(a, []), [0, 0])
  br = bisect_right(p.get(a, []), [x, y])

  bl2 = bisect_left(p.get(a, []), [0, 0])
  br2 = bisect_left(p.get(a, []), [x, y])
  
  t = max(t, abs(br-bl), abs(br2-bl2))
print(t)
