from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for i in range(n+1)]
dis = [1e9 for i in range(n+1)]

for _ in range(e):
  s, e, c = map(int, input().split())
  graph[s].append([e, c])
  graph[e].append([s, c])

u, v = map(int, input().split())

def ds(start, end, d):
  q = []
  heappush(q, [0, start])
  d[start] = 0

  while q:
    cur_c, cur = heappop(q)
    if d[cur] < cur_c: continue
    for i, c in graph[cur]:
      if d[cur] + c < d[i]:
        d[i] = d[cur] + c
        heappush(q, [d[i], i])

  return d[end]

def f(l, dis):
  total = 0
  for s, e in l:
    cost = ds(s, e, dis[:])
    if cost == 1e9: return 1e9
    total += cost
  return total

a = f([[1, v], [v, u], [u, n]], dis[:])
b = f([[1, u], [u, v], [v, n]], dis[:])

if a == 1e9 and b == 1e9: print(-1)
else: print(min(a, b))
