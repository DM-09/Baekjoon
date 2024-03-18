l = [input().split() for _ in range(10)]

for i in l:
  if len(set(i)) == 1: print(1); exit()

for i in range(10):
  a = set()
  for j in range(10): a.add(l[j][i])
  if len(a) == 1: print(1); exit()

print(0)
