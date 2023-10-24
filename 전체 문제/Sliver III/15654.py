from itertools import *

n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in sorted(permutations(a, m)):
    print(' '.join(map(str, i)))
