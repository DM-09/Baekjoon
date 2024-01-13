from math import *

a, b = map(int, input().split())
c = abs(a - b)

for _ in range(gcd(gcd(a, b), c)): print('1', end="")
