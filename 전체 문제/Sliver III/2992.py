from itertools import permutations

n = input()
per = list(permutations(list(n)))

for i in sorted(per):
    new = int(''.join(i))
    if new > int(n):
        print(new)
        break
else: print(0)
