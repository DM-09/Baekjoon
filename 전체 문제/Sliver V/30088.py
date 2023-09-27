inp = lambda: input().strip()
n = int(inp())
r, s = [], 0

for _ in range(n):
     a = list(map(int, inp().split()))
     num = a.pop(0)
     r.append(sum(a))

r.sort()

for i in range(len(r)):
     s += sum(r)
     r.pop()

print(s)
