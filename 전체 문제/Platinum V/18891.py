P, V = map(int, input().split())
party = [253]
cparty = []
allV = 0
cv = 0
NmR = 300

for i in range(P):
  name, r, v = input().split()
  r, v = int(r), int(v)

  party.append([name, r, v])

  allV += v
  party[0] -= r

for i in range(1, P+1):
  _, r, v = party[i]
  if (v / allV * 100) >= 3 or r >= 5:
    cparty.append(i)
    cv += v
  else: NmR -= r

sps = []
ps = {}

NmR -= party[0]

for i in cparty:
  _, r, v = party[i]
  p = v / cv

  ps[i] = p
  a = (NmR * p - r) / 2

  if a < 1: a = 0
  else: a = int(round(a))

  sps.append([i, a])

sumSp = sum([j for i, j in sps])
req1 = []
req2 = []
left_30, left_17 = 30, 17

for i, sp in sps:
  if sumSp == 30: break
  if sumSp < 30:
    a = sp + (30 - sumSp) * ps[i]
  elif sumSp > 30:
    a = (30 * sp) / sumSp

  num, pr = int(a), str(a).split('.')[1]
  party[i][1] += num
  left_30 -= num

  req1.append([pr, -i])

for i in cparty:
  p = ps[i]
  a = 17 * p
  num, pr = int(a), str(a).split('.')[1]
  req2.append([pr, -i])
  left_17 -= num
  party[i][1] += num

for _, i in sorted(req1)[::-1]:
  i = -i
  if left_30 <= 0: break
  party[i][1] += 1
  left_30 -= 1

for _, i in sorted(req2)[::-1]:
  i = -i
  if left_17 <= 0: break
  party[i][1] += 1
  left_17 -= 1

for i in sorted(party[1:], key=lambda x: (-x[1], x)):
  print(i[0], i[1])
