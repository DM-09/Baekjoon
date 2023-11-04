n = int(input())
l = [int(input()) for _ in range(n)]

m = max(l)
dp = [0] * (m + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for i in range(5, m + 1):
  dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for i in l:
  print(dp[i])
