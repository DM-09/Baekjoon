from itertools import *

n, m = map(int, input().split())
a = [i + 1 for i in range(n)]

for i in sorted(combinations_with_replacement(a,  m)):
    print(' '.join(map(str, i)))
