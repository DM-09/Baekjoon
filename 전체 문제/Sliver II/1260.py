from collections import deque

N, M, V = map(int, input().split())
graph = {}

def dfs(root):
  visited = []
  todo = deque([root])

  while len(todo) != 0:
    cur = todo.popleft()
    if not cur in visited: 
      visited.append(cur)

      if graph.get(cur, 'not') != 'not':
        get = graph[cur]
        for i in sorted(get)[::-1]:
          if not i in visited: todo.appendleft(i)
  
  return visited

def bfs(root):
  visited = []
  todo = deque([root])

  while len(todo) != 0:
    cur = todo.popleft()
    if not cur in visited: 
      visited.append(cur)

      if graph.get(cur, 'not') != 'not':
        get = graph[cur]
        for i in sorted(get):
          if not i in visited: todo.append(i)
  
  return visited

for i in range(M):
  a, b = map(int, input().split())
  try: graph[a].append(b)
  except: graph[a] = [b]
    
  try: graph[b].append(a)
  except: graph[b] = [a]

print(*dfs(V))
print(*bfs(V))


