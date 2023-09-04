from math import *
from itertools import *

for _ in range(int(input())):
    l = list(combinations(list(map(int, input().split())), 2))
    n = 0

    for i in l:
        x, y = i[0], i[1]
        g = gcd(x, y)
        n = max(n, g)
    print(n)
