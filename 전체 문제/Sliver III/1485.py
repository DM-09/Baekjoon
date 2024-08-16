def Lm(q, w):
  a, b = q
  c, d = w
  return abs(a-c) + abs(b-d)

for _ in range(int(input())):
  p = [list(map(int,input().split())) for _ in ' '*4]
  p.sort(key=lambda x:(x[0], x[1]))
  s = set([Lm(p[0], p[1]), Lm(p[1], p[3]), Lm(p[3], p[2]), Lm(p[0], p[2])])
  print(+(len(s)==1 and Lm(p[0], p[3]) == Lm(p[1], p[2])))
