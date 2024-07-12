n = int(input())
s = list(input())

d = {}
A, B = [], []
taken = [0] * n

for i in range(n): d[i] = s[i]
d = sorted(d.items(), key=lambda x: (-ord(x[1]), x[0]))

for i in range(n):
  if i % 2 == 0:
    while taken[len(s)-1] and s: s.pop()
    if not s: break
    taken[len(s)-1] = 1; A.append(s.pop())
  else:
    while d:
      a, b = d.pop()
      if taken[a] == 0:
        taken[a] = 1
        B.append(b)
        break

if sorted([A, B])[0] == B and A != B: print('DA')
else: print('NE')
print(''.join(B))
