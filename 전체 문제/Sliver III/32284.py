n, m = map(int, input().split())
a, b = map(int, input().split())

Map = [['O' for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    if j < b: Map[i][j] = 'E'
    else: Map[i][j] = 'W'

for i in range(n):
  if i < a: Map[i][b] = 'S'
  else: Map[i][b] = 'N'

for i in Map: print(''.join(i))
