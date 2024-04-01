from decimal import *
getcontext().prec = 200

for _ in range(int(input())):
  l = []
  while 1:
    i = input()
    if i == '0': break
    l.append(Decimal(i))
  a = list(str(sum(l)))
  while 1:
    if a[-1] == '0': a.pop()
    elif a[-1] == '.': a.pop(); break
    else: break
  print(''.join(a))
