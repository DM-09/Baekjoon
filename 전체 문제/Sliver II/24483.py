from collections import deque
import sys

input = sys.stdin.readline

graph = {}

def dfs(root, graph : dict, n):
    todo = deque([(root, 0)])
    visited = []
    table = [1] * (n + 1)
    
    while todo:
        cur = todo.popleft()
        c, d = cur[0], cur[1]
        
        if table[c]:
            table[c] = 0
            visited.append([c, d])
            re = graph.get(c, '0')
            
            if re != '0':
                for i in sorted(re)[::-1]:
                    todo.appendleft([i, d + 1])
    return visited

n, m, r = map(int, input().split())

for _ in range(m):
    u, v = map(int, input().split())
    try: graph[u].append(v)
    except: graph[u] = [v]
    
    try: graph[v].append(u)
    except: graph[v] = [u]
    
res = dfs(r, graph, n)
ans = 0
for j in range(len(res)):
    i = res[j]
    # print((j+1), i[1], 0)
    ans += (j+1) * i[1]

print(ans)
