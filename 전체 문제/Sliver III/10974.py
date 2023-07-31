from itertools import permutations

l = [str(i + 1) for i in range(int(input()))]

for c in sorted(permutations(l)): print(' '.join(c))
