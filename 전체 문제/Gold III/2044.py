m, n = map(int, input().split())
d = {}
todo = []
picture = [['.' for _ in range(n)] for _ in range(m)]

for _ in range(m):
  s = input()
  f, start, end = True, 0, 0
  l = []
  a = []

  ind = -1
  for i in s:
    ind += 1
    if i != '+' and f: continue
    l.append(i)

    if i == '+':
      if f: start = ind;
      else: end = ind
      f = not f
    if i == '+':
      if len(a) == 0: l = [l.pop()]; continue
      key = ''.join(a)
      d[key] = [''.join(l)]
      todo.append([key, [start, end]])
      l = []
      a = []
    if i in 'abcdefghijklmnopqrstuvwxyz': a.append(i)
  for i in sorted(todo, key=lambda x: x[1]):
    key, start, end = i[0], i[1][0], i[1][1]
    q = s[start:end+1]

    if q.count('-|'): continue
    if not q.count('|') and not q.count('+'): continue

    d[key].append(q)
    if q.count('+'): todo.remove(i)

a = 0
for i in sorted(d):
  q = d[i]
  for j in range(len(q)):
    for k in range(len(q[j])):
      picture[j+a][k+a] = q[j][k]
  a += 1

for i in picture:
  print(''.join(i))
