n = int(input())
q = input()

s, b, a = q.count('S'), q.count('B'), q.count('A')

if s == b == a: print('SCU')
else:
    m = max([s, b, a])
    if b == m: print('B', end='')
    if s == m: print('S', end='')
    if a == m: print('A')
