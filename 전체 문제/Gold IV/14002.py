n = int(input())
a = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
  c = a[i]
  dp[i] = [1, [c]]

  for j in range(i):
    dpj = dp[j]
    if a[i] > a[j] and dp[i][0] >= dp[j][0]: dp[i] = max(dp[i], [dpj[0]+1, dpj[1] + [c]])
    elif a[i] == a[j]: dp[i] = [dpj[0], dpj[1]]

m = max(dp)
print(m[0])
print(*m[1])
