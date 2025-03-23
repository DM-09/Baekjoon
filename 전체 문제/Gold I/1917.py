def check(box):
  for i in range(4):
    for j in range(4):
      a = [list('0000'), list('1111'), list('0000')]
      b = [list('010') for _ in 'a' * 4]
      a[0][i] = '1'
      a[2][j] = '1'
      b[i][0] = '1'
      b[j][2] = '1'

      for cur in [a, b]:
        if cur in box or cur[::-1] in box: return 'yes'

  for i in [[list('0011'), list('0110'), list('1100')],
            [list('0011'), list('1110'), list('1000')],
            [list('0100'), list('1110'), list('0011')],
            [list('1100'), list('0111'), list('0100')],
            [list('00111'), list('11100')]]:
    j = [q[::-1] for q in i]
    k = [[j[w][q] for w in range(len(i))] for q in range(len(i[0]))]
    l = [q[::-1] for q in k]

    for cur in [i, j, k, l]:
      if cur in box or cur[::-1] in box: return 'yes'

  return 'no'

for _ in 'a'*3:
  m = [input().replace(' ','') for i in 'a'*6]
  box = []

  for i in range(4):
    for j in range(3): box.append([list(m[i+k][j:j+4]) for k in range(3)])

  for i in range(3):
    for j in range(4): box.append([list(m[i+k][j:j+3]) for k in range(4)])

  for i in range(5):
    for j in range(2): box.append([list(m[i+k][j:j+5]) for k in range(2)])

  for i in range(2):
    for j in range(5): box.append([list(m[i+k][j:j+2]) for k in range(5)])

  print(check(box))
