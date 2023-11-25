for _ in range(int(input())):
  x1, y1, r1, x2, y2, r2 = map(int,input().split())
  code = 0
  distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
  
  if [x1, y1, r1] == [x2, y2, r2]: code = -1
  elif r1 + r2 == distance or (a := abs(r1 - r2)) == distance: code = 1
  elif r1 + r2 > distance and a < distance: code = 2

  print(code)
