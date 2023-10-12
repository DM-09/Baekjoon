graph = {}
n = int(input())
m = int(input())

for _ in range(m):
    a, b = map(int, input().split())

    try: graph[a].append(b)
    except: graph[a] = [b]

    try: graph[b].append(a)
    except: graph[b] = [a]


if graph.get(1, 0):
    s = set()
    for i in graph[1]: # 2 3 4
        for j in graph[i]:
            s.add(j)
        s.add(i)
    print(len(s) - 1)
else: print(0)
