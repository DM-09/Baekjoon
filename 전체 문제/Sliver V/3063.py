for _ in range(int(input())):
  x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
  S_poster1 = (x2 - x1) * (y2 - y1)

  ny1, ny2 = y3, y4
  if y3 < y1: ny1 = y1
  if y4 > y2: ny2 = y2

  if y4 < y1: ny1 = ny2 = 0
  if y3 > y2: ny1 = ny2 = 0

  nx1, nx2 = x3, x4
  if x3 < x1: nx1 = x1
  if x4 > x2: nx2 = x2

  if x3 > x2: nx1 = nx2 = 0
  if x4 < x1: nx1 = nx2 = 0

  S_overlap = (nx2 - nx1) * (ny2 - ny1)
  print(S_poster1 - S_overlap)
