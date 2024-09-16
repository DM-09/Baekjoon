w = {input() : 0 for _ in range(int(input()))}
n = {}

for i in w:
  for j in w: n[i+j] = 0

for _ in range(int(input())):
  a = input()
  if a in w: print(1)
  elif a in n: print(2)
  else: print(0)
