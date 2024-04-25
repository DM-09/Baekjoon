n = int(input())
a = list(input())

dp = [[0 for _ in range(n+1)] for i in range(n+1)]

for i in range(n):
  for j in range(n):
    if a[i] == a[-1-j]: dp[i+1][j+1] = dp[i][j] + 1
    else: dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(n - dp[-1][-1])
