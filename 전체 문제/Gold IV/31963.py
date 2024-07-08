n = int(input())
a = list(map(int, input().split()))

l = [0] * (n + 1)

for i in range(1, n):
  c = 0
  q, w = a[i-1], a[i]
  if q <= w:
    e = q
    for j in range(21):
      e *= 2
      if e == w: c = -j-1; break
      elif e > w: c = -j; break
  else:
    for j in range(21):
      if q <= w: c = j; break
      w *= 2
  l[i] = c

ans = 0

for i in range(1, n):
  if l[i] > 0: ans += l[i]; l[i+1] += l[i]

print(ans)
