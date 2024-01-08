from math import factorial as f
import sys

input = sys.stdin.readline

graph = {}
n, m = map(int, input().split())

for i in range(m):
    u, v = map(int, input().split())
    try: graph[u].append(v)
    except: graph[u] = [v]
    try: graph[v].append(u)
    except: graph[v] = [u]

a = 0
for i in range(n):
    c = len(graph.get(i + 1, ""))
    if c >= 3: a += f(c) // (6 * f(c-3))

print(a  % (10 ** 9 + 7))
