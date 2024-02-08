a = input()
b = input()

dp = [[[0, ''] for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(len(a)):
    for j in range(len(b)):
        dpj = dp[i][j]
        if a[i] == b[j]: dp[i+1][j+1] = [dpj[0]+1, dpj[1]+a[i]]
        else: dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(*dp[-1][-1])
