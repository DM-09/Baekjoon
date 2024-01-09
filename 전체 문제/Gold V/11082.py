from fractions import Fraction
from math import *

def inf(i):
    integer, decimal = i.split('.')
    a, b = decimal[:-1].split('(')
    x, y = 10 ** len(a + b), 10 ** len(a)

    c = int(integer + a + b) - int(integer + a)
    d = x - y

    GCD = gcd(c, d)
    return f'{str(c // GCD)}/{str(d // GCD)}'

i = input()
if i.count('('): print(inf(i))
elif i.count('.') == 0: print(i+'/1')
else:
    h, t = i.split('.')[0], i.split('.')[1]
    a = int('1' + ('0' * len(t)))
    b = int(Fraction(i) * a)
    g = gcd(a, b)
    print(f'{b // g}/{a // g}')
