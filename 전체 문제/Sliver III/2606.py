from collections import deque

n, m = int(input()), int(input())
graph = {}
table = [0] * (n + 1)

def bfs(root, n):
    rode = []
    visited = [1] * (n + 1)
    todo = deque([root])

    while todo:
        cur = todo.popleft()
        if visited[cur]:
            visited[cur] = 0
            rode.append(cur)
            table[cur] = 1
            if graph.get(cur, '1') != '1':
                for i in sorted(graph[cur]):
                    if visited: todo.append(i)

    return rode

for _ in range(m):
    u, v = map(int, input().split())

    try: graph[u].append(v)
    except: graph[u] = [v]

    try: graph[v].append(u)
    except: graph[v] = [u]

bfs(1, n)
print(sum(table) - 1)
