def getIndex(l, v):
  if v in l: return l.index(v)
  return len(l)

for _ in range(int(input())):
  s = input().split()
  c = len(s) // 2 - 1

  while 'X' in s:
    if c == 0: break
    i = s.index('X')
    a = f'({s[i-1]} X {s[i+1]})'
    c -= 1
    del s[i+1], s[i], s[i-1]
    s.insert(i-1, a)

  for _ in range(c):
    i = min(getIndex(s, '+'), getIndex(s, '-'))
    a = f'({s[i-1]} {s[i]} {s[i+1]})'
    del s[i+1], s[i], s[i-1]
    s.insert(i-1, a)

  print(' '.join(s))
  print()
