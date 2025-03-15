n = int(input())
ans = 1
g1, g2, g3 = 0, 0, 0

for i in range(1, n+1):
  r = i % 3
  if r == 1:
    ans += g2 + g3 + 1
    g1 += 1
  elif r == 2:
    ans += g1 + g2 + 1
    g3 += 1
  else:
    ans += g1 + g3 + 1
    g2 += 1

print(ans)
