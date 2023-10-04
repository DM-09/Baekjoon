from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
table = [0] * n

graph = {}

def dfs(root, n):
    visited = [1] * (n + 1)
    rode = []
    todo = deque([root])

    while len(todo) != 0:
        cur = todo.popleft()
        if visited[cur]:
            visited[cur] = 0
            rode.append(cur)

            if graph.get(cur, '1') != '1':
                for i in sorted(graph[cur]):
                    if visited[i]: todo.appendleft(i)

    return rode

for _ in range(m):
    u, v = map(int, input().split())

    try: graph[u].append(v)
    except: graph[u] = [v]

    try: graph[v].append(u)
    except: graph[v] = [u]

re = dfs(r, n)
for i in range(len(re)): table[re[i] - 1] = i + 1

print(*table)
