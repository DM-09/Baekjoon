n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
MAX = max(map(len, m)) - 1

for i in range(1, MAX + 1):
    s = set()

    for j in m: s.add(str(m[:i]))
    if len(s) == n: print(i); break

else: print(MAX)
