from math import degrees, acos

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
e, f = list(map(int, input().split()))

def isLine(a, b, c, d, e, f):
  return (a*d + c*f + e*b) - (a*f + e*d + c*b) == 0

def getLen(x1, y1, x2, y2):
  q, w = x1-x2, y1-y2
  return (q*q + w*w) ** .5

def getDeg(l1, l2, l3):
  return round(degrees(acos((l1**2 + l2**2 - l3**2)/(2.0 * l1 * l2))), 5)

if isLine(a,b,c,d,e,f): exit(print('X'))
 
l1, l2, l3 = getLen(a,b,c,d), getLen(a,b,e,f), getLen(c,d,e,f)
r1, r2, r3 = getDeg(l3,l2,l1), getDeg(l1,l3,l2), getDeg(l2,l1,l3)
mr = max([r1, r2, r3])

if l1 == l2 == l3: print('JungTriangle')
elif len(set([l1, l2, l3])) == 2:
  if mr > 90: print('Dunkak2Triangle')
  elif mr == 90: print('Jikkak2Triangle')
  else: print('Yeahkak2Triangle')
else:
  if mr > 90: print('DunkakTriangle')
  elif mr == 90: print('JikkakTriangle')
  else: print('YeahkakTriangle')
