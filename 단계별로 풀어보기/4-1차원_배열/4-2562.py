l = []

for i in range(9):
   inp = int(input())
   l.append(inp)

m = max(l)

for e in range(len(l)):
    if l[e] == m:
        print(m,
              e + 1)
