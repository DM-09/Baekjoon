n = int(input())
a = list(map(int, input().split()))
NGE = [-1] * n

stk = [0]

for i in range(1, n):
  while stk and a[stk[-1]] < a[i]:
    NGE[stk.pop()] = a[i]
  stk.append(i)

print(*NGE)
