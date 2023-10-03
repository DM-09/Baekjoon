from collections import deque
import sys

input = sys.stdin.readline

graph = {}

n, m = map(int, input().split())

num = 0
s = set()
visit = [1] * n

def dfs(root):
    visited = []
    todo = deque([root])

    while len(todo) != 0:
        cur = todo.popleft()
        if not cur in visited:
            visited.append(cur)

            if graph.get(cur, '1') != '1':
                get = graph[cur]
                for i in get:
                    if not i in visited: todo.appendleft(i)
                    visit[i - 1] = 0

    return visited

for _ in range(m):
    u, v = map(int, input().split())

    try: graph[u].append(v)
    except: graph[u] = [v]

    try: graph[v].append(u)
    except: graph[v] = [u]

for i in range(len(visit)):
    if visit[i]: dfs(i + 1); num += 1
print(num)
