n, m, y, x, k = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]

query = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

method = {1: [[0, 4], [0, 2], [0, 5]], 3: [[0, 1], [0, 2], [0, 3]]}
method[2] = method[1][::-1]
method[4] = method[3][::-1]

move = {1: (1, 0), 2: (-1, 0), 3: (0, -1), 4: (0, 1)}

for q in query:
  mx, my = move[q]
  x += mx
  y += my

  if not (0 <= x < m and 0 <= y < n): x -= mx; y -= my; continue
  for i, j in method[q]: dice[i], dice[j] = dice[j], dice[i]

  a = Map[y][x]
  if a: Map[y][x] = 0; dice[2] = a
  else: Map[y][x] = dice[2]

  print(dice[0])
