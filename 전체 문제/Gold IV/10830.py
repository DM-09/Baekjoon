from copy import deepcopy

def mt_mult(m, m2):
  n = len(m)
  new = [[0]*n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      new[i][j] = sum([m[i][k] * m2[k][j] for k in range(n)]) % 1000
  return new

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    a[i][j] = a[i][j] % 1000
    
l = [deepcopy(a)]

for i in range(36):
  l.append(mt_mult(l[i], l[i]))

s = bin(b)[2:][::-1]
q = []
for i in range(len(s)):
  if s[i] == '1': q.append(l[i])

t = deepcopy(q[0])
for i in range(len(q)-1):
  t = mt_mult(t, q[i+1])
  
for i in t: print(*i)
