from collections import defaultdict as dd

h, v = map(int, input().split())
ys = list(map(int, input().split()))
xs = list(map(int, input().split()))

y_list = dd(int)
x_list = dd(int)

for i in range(h):
  for j in range(i+1, h):
    a, b = ys[i], ys[j]
    y_list[b-a] += 1

for i in range(v):
  for j in range(i+1, v):
    a, b = xs[i], xs[j]
    x_list[b-a] += 1

ans = 0
for i in x_list: ans += y_list[i] * x_list[i] 
print(ans)
