from collections import defaultdict as dd

s = input()
t = input()

a = dd(int)

for i in range(len(t)-1): a[t[i]] = max(a[t[i]], i+1)

q, w = len(s), len(t)
m = [q+w, 0, 0]
for i in range(1, q):
  cur = s[i]
  j = a[cur]-1
  if j < 0: continue
  m = min(m, [i+w-j, i, j])

if m[1]+m[2] == 0: print(-1)
else: print(s[:m[1]]+t[m[2]:])
