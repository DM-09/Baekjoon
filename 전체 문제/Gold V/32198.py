n = int(input())
cases = sorted([list(map(int, input().split())) for _ in range(n)])
max_t = cases[-1][0]
inf = 9999
bb = 9998

dp = [[inf for _ in range(2002)] for _ in range(max_t+1)]

dp[0][1000] = 0

for t, l, r in cases:
  for i in range(l+1, r):
    dp[t][1000 + i] = bb

for i in range(max_t):
  for x in range(2001):
    if not dp[i][x] in [bb, inf]:
      if dp[i+1][x+1] != bb: dp[i+1][x+1] = min(dp[i+1][x+1], dp[i][x] + 1)
      if dp[i+1][x-1] != bb: dp[i+1][x-1] = min(dp[i+1][x-1], dp[i][x] + 1)
      if dp[i+1][x] != bb: dp[i+1][x] = min(dp[i+1][x], dp[i][x])

a = min(dp[-1])
if a < bb: print(a)
else: print(-1)
