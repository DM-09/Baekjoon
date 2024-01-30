n, w = map(int, input().split())
l = []

for _ in range(n):
  id = input()
  log = [input() for _ in range(7)]

  A = [0, 9999, 9999]
  cur = [0, 0, 0]

  streak, lf = False, 0
  day, fail = 0, 0
  for j in range(w):
    for i in range(7):
      a = log[i][j]
      if a == 'O':
        if not streak: cur[2] = day
        streak = True
        cur[1] += lf; lf = 0; cur[0] -= 1
      elif a == 'F' and streak: lf += 1
      elif a == 'X':
        fail += 1; streak = False; lf = 0
        A = min(A, cur)
        cur = [0, 0, 0]
      day += 1
  A = min(A, cur)
  l.append((A[0], A[1], A[2], fail, id))

rank = 0
pre = []

for i in sorted(l):
  if pre != i[:-1]: rank += 1
  pre = i[:-1]
  print(f'{rank}. {i[4]}')
