from math import *
dp = [[0 for _ in range(320)] for _ in range(1002)]
n = int(input())

dp[1][0] = 1
dp[2][0] = 1
dp[3][0] = 1

for i in range(4, n+1):
    a = int(i//pi)
    dp[i][a] = 1
    for j in range(1, a): dp[i][a-j] = dp[i-1][a-j] + dp[i][a-j+1]
    dp[i][0] = (dp[i-1][0] + dp[i][1]) % 10**18

print(dp[n][0])
