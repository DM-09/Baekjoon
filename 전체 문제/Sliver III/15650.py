from itertools import *
n, m = map(int, input().split())

for i in combinations([i + 1 for i in range(n)], m): print(*i)
