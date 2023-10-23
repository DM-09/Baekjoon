from collections import deque
import sys

input = sys.stdin.readline

graph = {}

def bfs(root, graph, num):
    visited, todo = [], deque([root])
    notVisit = [1] * (num + 1)
    depth, d = [], 0
    box = []

    while todo:
        cur = todo.popleft()

        if notVisit[cur]:
            visited.append(cur)
            notVisit[cur] = 0
            depth.append(d)
            get = graph.get(cur, '0')

            if get != '0':
                for i in sorted(get): box.append(i)

        if not todo:
            todo = deque(box)
            box = []
            d += 1

    return visited, depth

n, m, r = map(int, input().split())

for _ in range(m):
    u, v = map(int, input().split())

    try: graph[u].append(v)
    except: graph[u] = [v]

    try: graph[v].append(u)
    except: graph[v] = [u]

res = bfs(r, graph, n)
ans = 0

for i in range(len(res[0])):
    ans += (i + 1) * res[1][i]

print(ans)
