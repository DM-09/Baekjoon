n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
for i in range(0, 10): dp[1][i] = 1

if n == 1: exit(print(10))

for t in range(2, n+1):
  for a in range(10):
    dp[t][a] = sum(dp[t-1][:a+1])

print(sum(dp[-1]) % 10007)
