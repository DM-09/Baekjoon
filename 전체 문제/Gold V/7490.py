from itertools import *

for _ in range(int(input())):
    n = int(input())
    l = [i+1 for i in range(n)]

    for i in sorted(set(combinations(['+', '-', ' '] * (n-1), n-1))):
        i = list(i)
        i.append(1)
        i = i[::-1]

        new = []
        for j in l: new.append(j); new.append(i.pop())
        new.pop()

        s = ''.join(list(map(str, new)))
        if eval(s.replace(' ', '')) == 0: print(s)
    print()
