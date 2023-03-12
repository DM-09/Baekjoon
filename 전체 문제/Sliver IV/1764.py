N, M = map(int, input().split())
l = {}
t = set()

for i in range(N + M):
    s = input()
    try:
        l[s] += 0
        t.add(s)
    except KeyError:
        l[s] = 1

print(len(t))
t = list(t)
t.sort()
for i in range(len(t)):
    print(t[i])
