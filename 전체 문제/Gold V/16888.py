square = [i*i for i in range(1,1001)]
dp = [0] * (10**6 + 1)
squ_ind = 0
dp[0] = 2
dp[1] = 1

for i in range(2, 10**6+1):
  if (i**.5).is_integer(): squ_ind += 1
  for j in range(squ_ind+1):
    if dp[i-square[j]] == 2:
      dp[i] = 1
      break
    else: dp[i] = 2

for _ in range(int(input())):
  n = int(input())
  print('koosaga' if dp[n] == 1 else 'cubelover')
