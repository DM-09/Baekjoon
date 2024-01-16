import math

def fpow(a, b, c):
  if b == 1:
    return a % c
  else:
    if b % 2 == 0:
      return (fpow(a, b//2, c) ** 2) % c
    else:
      return ((fpow(a, b//2, c) ** 2) * a) % c

while 1:
    p, a = map(int, input().split())
    if p + a == 0: break
    power = fpow(a, p, p)

    if power == a:
        for i in range(2, int(math.sqrt(p))):
            if p % i == 0: print('yes'); break
        else: print('no')
    else: print('no')
