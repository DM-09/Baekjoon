import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
p = {tuple(map(int, input().split())) : 1 for _ in range(n)}

c = set()

for i, j in p:
  p1, p2, p3 = (i+a, j), (i, j+b), (i+a, j+b)
  p4, p5, p6 = (i-a, j), (i, j-b), (i-a, j-b)
  p7, p8 = (i-a, j+b), (i+a, j-b)

  r = [0, p.get(p1, 0), p.get(p2, 0), p.get(p3, 0), p.get(p4, 0), p.get(p5, 0), p.get(p6, 0), p.get(p7, 0), p.get(p8, 0)]

  cp = (i, j)
  if r[1] + r[2] + r[3] == 3: c.add(str(sorted([p1, p2, p3, cp])))
  if r[4] + r[5] + r[6] == 3: c.add(str(sorted([p4, p5, p6, cp])))
  if r[1] + r[5] + r[8] == 3: c.add(str(sorted([p1, p5, p8, cp])))
  if r[4] + r[2] + r[7] == 3: c.add(str(sorted([p4, p2, p7, cp])))
    
print(len(c))
