from itertools import *

n, m = map(int, input().split())
l = list(map(int, input().split()))

r = combinations_with_replacement(l, m)
s = set(str(sorted(list(i)))[1:-1].replace(',', '') for i in r)

for i in sorted(list(map(int, j.split())) for j in s): print(*i)
