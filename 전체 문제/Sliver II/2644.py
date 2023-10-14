from collections import deque

graph = {}

def bfs(root, n):
    visited = []
    nv = [1] * (n + 1)
    todo = deque([root])
    next = []
    count = 0

    while todo:
        cur = todo.popleft()
        if nv[cur]:
            nv[cur] = 0
            visited.append(cur)
            if graph.get(cur, '1') != '1':
                for i in sorted(graph[cur]):
                    if i == p2: return count + 1
                    if nv: next.append(i)
        if not todo:
            todo = deque(next)
            next = []
            count += 1
    return -1

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

for _ in range(m):
    u, v = map(int, input().split())

    try: graph[u].append(v)
    except: graph[u] = [v]

    try: graph[v].append(u)
    except: graph[v] = [u]

print(bfs(p1, n))
