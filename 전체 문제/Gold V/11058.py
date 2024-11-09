n = int(input())
dp = [[0, 0]] * 101

dp[1] = [1, 0]
dp[2] = [2, 0]
dp[3] = [3, 0]
dp[4] = [4, 0]
dp[5] = [5, 0]

for i in range(6, n+1):
  choice1 = [dp[i-1][0]+dp[i-1][1], dp[i-1][1]]
  choice2 = [dp[i-3][0]*2, dp[i-3][0]]
  choice3 = [dp[i-4][0]*3, dp[i-4][0]]

  dp[i] = max([choice1, choice2, choice3])

print(dp[n][0])
