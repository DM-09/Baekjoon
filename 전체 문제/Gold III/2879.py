n = int(input())
l = list(map(int, input().split()))
c = list(map(int, input().split()))

dis = [c[i] - l[i] for i in range(n)]

def search(dis):
  pre_sign = dis[0] > 0 if dis[0] else -1
  Max = [0, 0, 1, pre_sign]
  box = [0, 0, 1, pre_sign]

  for k in range(1, n):
    cur = dis[k]
    sign = cur > 0 if cur else -1
    
    if cur != 0 and sign == pre_sign:
      box[1] += 1
      box[2] += 1
    else:
      Max = max(Max, box, key=lambda x: x[2])
      box = [k, k, 1, sign]
    pre_sign = sign

  return max(Max, box, key=lambda x: x[2])

ans = 0
while 1:
  i, j, m, s = search(dis)
  if i == j: break
  for k in range(i, j+1): dis[k] += 1*(-1 if s else 1)
  ans += 1

print(ans + sum([abs(i) for i in dis]))
