dp = [0] * 1001

dp[1] = 'CY'
dp[2] = 'SK'
dp[3] = 'CY'
dp[4] = 'SK'

n = int(input())

for i in range(5, n + 1):
    if dp[i - 4] == 'CY' or dp[i - 3] == 'CY' or dp[i - 1] == 'CY':
        dp[i] = 'SK'
    else: dp[i] = 'CY'

print(dp[n])
