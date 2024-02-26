n = int(input())
if n == 1: print('*'); exit()
l = ["*****", "***", "*"]

for i in range(3, n+1):
  m = len(l) * 2 + 1
  b = 1
  box = []
  if i % 2:
    box.append('*')
    for _ in range(len(l)-1):
      box.append('*' + ' ' * b + '*')
      b += 2
    b = 0
    for j in l:
      blank = ' ' * b
      box.append('*' + blank + j + blank + '*')
      b += 2
    box.append('*' * (m * 2 - 1))
  else:
    box.append('*' * (m * 2 - 1))
    b = 2 * len(l) - 2
    for j in l:
      blank = ' ' * b
      box.append('*' + blank + j + blank + '*')
      b -= 2
    b = len(l[-1])
    for i in range(len(l)-1):
      b -= 2
      blank = ' ' * b
      box.append('*' + blank + '*')
    box.append('*')
  l = box

if l[0] == '*':
  b = len(l) - 1
  for i in l: print(' ' * b + i); b -= 1
else:
  b = 0
  for i in l: print(' ' * b + i); b += 1
