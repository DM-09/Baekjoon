def getScore(x, y=1, z=None):
  return bin(x^y^z if z else x^y).count('1')


n = int(input())
cards = list(map(int, input().split()))
dp = [0] * (n+1)

if n < 4: exit(print([0, getScore(*cards)][+n!=1]))

dp[2] = getScore(*cards[:2])
dp[3] = getScore(*cards[:3])
dp[4] = dp[2] + getScore(*cards[2:4])

for i in range(5, n+1):
  dp[i] = max(dp[i-2] + getScore(*cards[i-2:i]), dp[i-3] + getScore(*cards[i-3:i]))

print(dp[-1])
