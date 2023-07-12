import sys
sys.setrecursionlimit(10 ** 6)

l = []
num, k = map(int, input().split())

def bout(n, s):
    if n == num:
        l.append(s)
        return 1
    if n >= num:
        return 0
    return bout(n + 1, s + '1+') + bout(n + 2, s + '2+') + bout(n + 3, s + '3+')


bout(0, '')
try: print(l[k-1][:-1])
except: print(-1)
