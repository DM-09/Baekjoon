def isPoint(a, b):
  bottomY, topY, leftX, rightX = a[0][1], a[1][1], a[0][0], a[2][0]
  xo1 = b[0][0] == rightX or b[2][0] == leftX
  xo2 = b[1][1] == bottomY or b[0][1] == topY
  if b[1][1] == bottomY and xo1: return True
  if b[0][1] == topY and xo1: return True
  if b[2][0] == leftX and xo2: return True
  if b[0][0] == rightX and xo2: return True
  return False

def isLine(a, b):
  bottomY, topY, leftX, rightX = a[0][1], a[1][1], a[0][0], a[2][0]
  xo1 = leftX <= b[0][0] <= rightX or rightX >= b[2][0] >= leftX
  xo2 = topY >= b[1][1] >= bottomY or bottomY <= b[0][1] <= topY
  if b[1][1] == bottomY and xo1: return True
  if b[0][1] == topY and xo1: return True
  if b[2][0] == leftX and xo2: return True
  if b[0][0] == rightX and xo2: return True
  return False

def isNull(a, b):
  bottomY, topY, leftX, rightX = a[0][1], a[1][1], a[0][0], a[2][0]
  if (b[2][0] < leftX or b[0][0] > rightX): return True
  if (b[1][1] < bottomY or b[0][1] > topY): return True
  return False


while 1:
  try: x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
  except: break

  a = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
  b = [(x3, y3), (x3, y4), (x4, y3), (x4, y4)]

  if isPoint(a, b) or isPoint(b, a): print('c')
  elif isLine(a, b) or isLine(b, a): print('b')
  elif isNull(a, b) or isNull(b, a): print('d')
  else: print('a')
