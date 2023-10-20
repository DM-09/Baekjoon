from collections import deque
import sys
input = sys.stdin.readline


graph = {}

def bfs(root, n, table):
    rode = []
    visited = [1] * (n + 1)
    todo = deque([root])
    b = []
    depth = 0

    while todo:
        cur = todo.popleft()
        if table[cur - 1] == -1:
            table[cur - 1] = depth

        if visited[cur]:
            visited[cur] = 0
            rode.append(cur)
            if graph.get(cur, '1') != '1':
                for i in sorted(graph[cur]):
                    if visited: b.append(i)

        if not todo:
            depth += 1
            todo = deque(b)
            b = []

    table[root - 1] = 0
    return table

n, m, r = map(int, input().split())
table = [-1] * n

for _ in range(m):
    u, v = map(int, input().split())

    try: graph[u].append(v)
    except: graph[u] = [v]

    try: graph[v].append(u)
    except: graph[v] = [u]

print(*bfs(r, n, table))
