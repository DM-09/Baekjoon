from math import *

while 1:
    try: i = input()
    except: break

    integer, decimal = i.split('.')
    a, b = decimal[:-1].split('(')
    x, y = 10 ** len(a + b), 10 ** len(a)

    c = int(integer + a + b) - int(integer + a)
    d = x - y

    GCD = gcd(c, d)
    print(f'{i} = {str(c // GCD)} / {str(d // GCD)}')
