from collections import deque
import sys
input = sys.stdin.readline

graph = {}

def dfs(root, n):
    visited = [1] * n
    rode = []
    todo = deque([root])

    while len(todo) != 0:
        cur = todo.popleft()
        if visited[cur]:
            visited[cur] = 0
            rode.append(cur)

            if graph.get(cur, '1') != '1':
                for i in sorted(graph[cur])[::-1]:
                    if visited[i]: todo.appendleft(i)

    return rode

n, m, r = map(int, input().split())

for _ in range(m):
    u, v = map(int, input().split())

    try: graph[u].append(v)
    except: graph[u] = [v]

    try: graph[v].append(u)
    except: graph[v] = [u]

table = [0] * n
re = dfs(r, n + 1)

for i in range(len(re)): table[re[i] - 1] = i + 1
print(*table)
