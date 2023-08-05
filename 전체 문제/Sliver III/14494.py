n, m = map(int, input().split())

dp = [[0 for _ in range(m)] for _ in range(n)]

def Get(x, y):
  l = [dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1]]
  return sum(l)

for i in range(n):
  for j in range(m):
    if (j == 0 or i == 0):
      dp[i][j] = 1
    else:
      dp[i][j] = Get(i,j)

print(dp[n-1][m-1] % 1000000007)
