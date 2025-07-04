from collections import defaultdict as dd, deque
import sys

input = sys.stdin.readline

graph = dd(list)

for _ in range(int(input())-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

ans = dd(int)

visited = dd(int)
a = dd(int)
todo = deque([1])
order = []

while todo:
  cur = todo.popleft()
  if visited[cur] == 0:
    visited[cur] = 1
    order.append(cur)
    for i in graph[cur]: todo.append(i)

for i in range(len(order)): a[order[i]] = i

for i in graph:
  if i == 1: continue
  n, m = 0, a[i]
  for j in graph[i]:
    b = a[j]
    if b < m: n, m = j, b
  ans[i] = n

print(' '.join(str(i[1]) for i in sorted(ans.items(), key=lambda x: x[0])))
