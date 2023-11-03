from itertools import *

n, m = map(int, input().split())
a = list(map(int, input().split()))

p = permutations(a, m)
p = sorted(set(p))

for i in p:
    print(' '.join(list(map(str, i))))
