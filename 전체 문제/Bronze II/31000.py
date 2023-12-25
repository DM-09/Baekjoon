n = int(input())

dp = [0] * 3001
dp[1] = 13
a = 26

for i in range(2, n+1):
    dp[i] = dp[i-1] + a
    a += 14

print(dp[n])
