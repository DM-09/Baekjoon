from heapq import *
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  q = []
  minh = []
  maxh = []
  ind = 0

  for _ in range(int(input())):
    t, n = input().split()
    n = int(n)

    if t == 'I':
      q.append(str(n))
      heappush(minh, (n, ind))
      heappush(maxh, (-n, ind))
      ind += 1
    elif n == 1 and maxh:
      while maxh:
        i = heappop(maxh)[1]
        if q[i] != '-': q[i] = '-'; break
    elif n == -1 and minh:
      while minh:
        i = heappop(minh)[1]
        if q[i] != '-': q[i] = '-'; break

  MAX, MIN = '', ''
  while maxh:
    i = heappop(maxh)[1]
    if q[i] != '-': MAX = q[i]; break

  while minh:
    i = heappop(minh)[1]
    if q[i] != '-': MIN = q[i]; break

  print("EMPTY" if MAX + MIN == '' else MAX, MIN)
