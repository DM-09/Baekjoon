t = int(input())
case = [int(input()) for _ in range(t)]
dp = [0] * 101

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(5, max(case) + 1):
  dp[i] = dp[i-1] + dp[i - 5]
  
for i in case: print(dp[i])
