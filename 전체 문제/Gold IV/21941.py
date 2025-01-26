from collections import defaultdict as dd

s = input()
n = len(s)
m = int(input())
d = dd(int)
dp = [0] * (n+1)

dp[n] = 0

for i in range(m):
  a, x = input().split()
  x = int(x)

  if x > len(a):
    d[a[::-1]] = max(d[a], x)
  

def choice2(s, d, dp, start):
  m = 0
  q = list(s)
  for i in range(len(s)):
    st = ''.join(q)
    cur = d[st]
    if cur > 0:
      m = max(m, dp[n - 1 - start + len(st)] + cur)
    _, *q = q
  return m

r = ''
for i in range(n):
  r += s[n-i-1]
  dp[n-i-1] = max(dp[n-i]+1, choice2(r, d, dp, i))

print(dp[0])
