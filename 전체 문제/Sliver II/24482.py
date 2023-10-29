from collections import deque
import sys
input = sys.stdin.readline

graph = {}

def dfs(root, graph: dict, n):
    todo = deque()
    table = [1] * (n + 1)
    ans = [-1] * n

    todo.append([root, 0])

    while todo:
        get = todo.popleft()
        cur, dep = get[0], get[1]

        if table[cur]:
            ans[cur - 1] = dep
            table[cur] = 0

            res = graph.get(cur, '0')
            if res != '0':
                for i in sorted(res):
                    todo.appendleft([i, dep + 1])

    return ans

n, m, r = map(int, input().split())

for _ in range(m):
    u, v = map(int, input().split())

    try: graph[u].append(v)
    except: graph[u] = [v]

    try: graph[v].append(u)
    except: graph[v] = [u]

table = [-1] * n
res = dfs(r, graph, n)

print(*res)
