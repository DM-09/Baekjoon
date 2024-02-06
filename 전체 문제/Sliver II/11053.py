n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1

for i in range(n):
  dp[i] = 1

  for j in range(i):
    if a[i] > a[j] and dp[i] >= dp[j]: dp[i] = max(dp[i], dp[j] + 1)
    elif a[i] == a[j]: dp[i] = dp[j]

print(max(dp))
