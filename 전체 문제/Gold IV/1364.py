n = int(input())
a = [0] * 6
ans = 0
for i in range(1, n+1):
  ans = i + a[i%6]
  if i == 6: ans += 1
  a[i%6] = ans
print(ans)
