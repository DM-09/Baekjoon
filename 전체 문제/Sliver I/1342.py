from itertools import permutations

p = permutations(input())
s = set()

for i in p:
    pre = ''

    for e in i:
        if e == pre: break
        pre = e
    else: s.add(''.join(i))

print(len(s))
