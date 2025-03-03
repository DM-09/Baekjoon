while 1:
  try: x1, y1, x2, y2, x3, y3 = map(float, input().split())
  except: break

  a = ((x1-x2)**2 + (y1-y2)**2)**.5
  b = ((x2-x3)**2 + (y2-y3)**2)**.5
  c = ((x3-x1)**2 + (y3-y1)**2)**.5

  s = (a + b + c) / 2
  k = (s*(s-a)*(s-b)*(s-c))**.5
  r = (a*b*c) / (4*k) * 2

  print(round(r*3.141592653589793, 2))
