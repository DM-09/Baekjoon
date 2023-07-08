dp = [[i + 1 for i in range(30)] for j in range(30)]

for i in range(1, 30):
  for j in range(i, 30):
    dp[i][j] = sum(dp[i-1][i-1:j])

for _ in range(int(input())):
  N, M = map(int, input().split())
  print(dp[N-1][M-1])
