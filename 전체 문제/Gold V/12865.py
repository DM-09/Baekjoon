item_count, total_weight = map(int, input().split())

items = []
dp = [[0 for _ in range(total_weight+1)] for _ in range(item_count+1)]

for i in range(item_count): items.append([*map(int, input().split())])

for i in range(1, item_count+1):
  for w in range(total_weight+1):
    iw, iv = items[i-1]
    if iw > w: dp[i][w] = dp[i-1][w]
    else: dp[i][w] = max(dp[i-1][w], iv + dp[i-1][w-iw])

print(dp[item_count][total_weight])
