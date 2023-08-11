n = int(input())
dp = [0] * (n + 4)

dp[1], dp[2], dp[3], dp[4] = 'SK', 'CY', 'SK', 'SK'

for i in range(5, n + 1):
    if dp[i - 1] == 'CY' or dp[i - 3] == 'CY' or dp[i - 4] == 'CY':
        dp[i] = 'SK'
    else: dp[i] = 'CY'

print(dp[n])
