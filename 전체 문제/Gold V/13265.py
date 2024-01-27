import sys
from collections import deque
input = sys.stdin.readline

def bfs(root, graph, colored):       
  todo = deque([(root, 0)])

  while todo:
    cur, color = todo.popleft()
    if colored[cur] == -1:
      colored[cur] = color
      color = 0 if color == 1 else 1
      for i in graph.get(cur,[]):
        todo.append((i, color))
    else:
      if colored[cur] != color: return (colored, False)
  return (colored, True)
    

for _ in range(int(input())):
  n, m = map(int, input().split())
  graph = {i+1: [] for i in range(n)}
  colored = [-1] * (n+1)
  r = 2

  for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

  for root in range(n):
    if colored[root+1] != -1: continue
    new_colored, result = bfs(root+1, graph, colored)
    colored = new_colored
    if result == False: r = 0; break
  
  print('impossible'[r:])
