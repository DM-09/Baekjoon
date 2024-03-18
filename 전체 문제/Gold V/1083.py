n = int(input())
a = list(map(int, input().split()))
s = int(input())

d = {}

for i in range(n):
  if s == 0: break
  for j in range(n): d[a[j]] = j
  b = sorted(a[i:])[::-1]

  for j in b:
    c = d[j] - i
    if c <= s:
      if 0 > c: break
      s -= c
      for k in range(c):
        a[c+i-k], a[c+i-k-1] = a[c+i-k-1], a[c+i-k]
      break

print(*a)
