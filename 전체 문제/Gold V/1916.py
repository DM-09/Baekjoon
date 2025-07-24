from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
d = [1e9 for i in range(n+1)]

for _ in range(int(input())):
  s, e, c = map(int, input().split())
  graph[s].append([e, c])

start, end = map(int, input().split())
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

print(d[end])
