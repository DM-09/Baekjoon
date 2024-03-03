n, s = map(int, input().split())
l = list(map(int, input().split()))

end = 0
ans = s+1
Sum = 0

for start in range(n):
  while Sum < s and end < n:
    Sum += l[end]
    end += 1
  if Sum >= s: ans = min(ans, end - start)
  Sum -= l[start]

if ans == s+1: ans = 0
print(ans)
