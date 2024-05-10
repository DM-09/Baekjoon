n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

x1, y1 = 0, 0
x2, y2 = 0, 0

for i in range(n):
  for j in range(m):
    if board[i][j] == 1:
      if x1 == y1 == 0: x1, y1 = i, j
      else: x2, y2 = i, j

print(abs(x2 - x1) + abs(y2 - y1))
