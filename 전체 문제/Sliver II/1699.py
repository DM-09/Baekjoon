n = int(input())

dp = [1] * (n + 1)
sq = [1]

for i in range(2, n + 1):
  if (i**.5).is_integer() and dp[i] == 1:
    sq.append(i)
    continue
  dp[i] = min(dp[i-j] + 1 for j in sq)

print(dp[n])
