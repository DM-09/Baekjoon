i = lambda: list(map(int, input().split()))
me = i()
p1 = i()
p2 = i()
p3 = i()

def getDis(x1, y1, x2, y2):
  pita = ((x1-x2)**2 + (y1-y2)**2)**.5
  xy = abs(x1-x2) + abs(y1-y2)
  if pita == 0: return xy
  return pita

ans = 1000
peo = [me, p1, p2, p3]
cur = me
val = 0

for i in [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]:
  for j in i:
    x, y = cur
    x1, y1 = peo[j]
    val += getDis(x, y, x1, y1)
    cur = [x1, y1]
  ans = min(ans, val)
  val = 0
  cur = me

print(int(ans))
