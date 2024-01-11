n = int(input())

def solve():
 for h in range(1, 10):
  for e in range(10):
   for l in range(10):
    for o in range(10):
     for w in range(1, 10):
      for r in range(10):
       for d in range(10):
        hello, world = int(f'{h}{e}{l}{l}{o}'), int(f'{w}{o}{r}{l}{d}')
        if len(set([h, e, l, o, w, r, d])) != 7: continue
        if hello + world == n:
            print(f'  {hello}')
            print(f'+ {world}')
            print('-------')
            if len(str(n)) == 5: print(f'  {n}')
            else: print(f' {n}')
            return
 print('No Answer')

solve()
