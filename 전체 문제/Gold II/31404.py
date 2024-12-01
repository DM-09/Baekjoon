h, w = map(int, input().split())
r, c, d = map(int, input().split())

A = [list(map(int, list(input()))) for _ in range(h)]
B = [list(map(int, list(input()))) for _ in range(h)]
Map = [list('1'*w) for _ in range(h)]

rot = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
last = -1
history = [[[1, 1, 1, 1] for _ in range(w)] for _ in range(h)]

while 1:
  cur = Map[r][c]
  if cur == '1':
    Map[r][c] = '0'
    d += A[r][c]
    d %= 4
    last = cnt + 1
  else:
    d += B[r][c]
    d %= 4
  r1, r2 = rot[d]
  r += r1
  c += r2
  cnt += 1

  if r < 0 or r >= h or c < 0 or c >= w: break

  if -history[r][c][d] == last: break
  history[r][c][d] = -cnt

print(last)
