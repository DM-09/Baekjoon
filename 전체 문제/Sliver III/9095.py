import sys
sys.setrecursionlimit(10 ** 6)

num = 0


def bout(n):
    if n == num:
        return 1
    if n >= num:
        return 0
    return bout(n + 1) + bout(n + 2) + bout(n + 3)


for _ in range(int(input())):
    num = int(input())
    print(bout(0))
