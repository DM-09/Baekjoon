
n = int(input())
a = list(map(int, input().split()))

def p(a):
  s = sum(a) / len(a)
  b = 0
  for i in a: b += ((i-s) ** 2)
  return round(b, 4)

for i in range(n):
  ans = [-1, -n]
  for j in range(n-i):
    l = a[j:i+1+j]
    ans = max(ans, [p(l), -j])
  print(-ans[1]+1)
