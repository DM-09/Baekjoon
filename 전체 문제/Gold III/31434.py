n, k = map(int, input().split())
market = [list(map(int, input().split())) for _ in range(n)]
market.sort(key = lambda x: x[1])
maxs = market[-1][1]*k + 1

dp = [[-1 for _ in range(maxs)] for _ in range(k+1)]
dp[0][1] = 0

for i in range(k):
  for j in range(maxs):
    if dp[i][j] == -1 or i + 1 > k:
      continue
    
    dp[i+1][j] = max(dp[i+1][j], dp[i][j] + j)

    for up in market:
      if j + up[1] >= maxs: continue
      dp[i + 1][j + up[1]] = max(dp[i + 1][j + up[1]], dp[i][j] - up[0])
    
print(max(dp[-1]))
