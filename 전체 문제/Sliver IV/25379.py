n = int(input())
l = list(map(int, input().split()))

ans1 = 0
ans2 = 0

a = 0
b = 0

for i in range(n):
  if l[i] % 2 == 0:
    ans1 += i - a
    a += 1

  else:
    ans2 += i - b
    b += 1

print(min(ans1, ans2))
