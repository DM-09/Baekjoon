n = int(input())
q, w, e, r, t, y = map(int, input().split())

for _ in range(n-1):
  a, b, c, i, j, k = map(int, input().split())
  q, w, e = max(a, q), max(b, w), max(c, e)
  r, t, y = min(r, i), min(t, j), min(y, k)

m, n, o = r - q, t - w, y - e

if min(m, n, o) < 0: print(0)
else: print(m * n * o)
