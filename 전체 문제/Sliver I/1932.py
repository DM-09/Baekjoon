n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n)]

dp[0][0] = a[0][0]

for j in range(n-1):
  for i in range(len(a[j])):
    dp[j+1][i] = max(dp[j][i] + a[j+1][i], dp[j+1][i])
    dp[j+1][i+1] = max(dp[j][i] + a[j+1][i+1], dp[j+1][i+1])

print(max(dp[-1]))
