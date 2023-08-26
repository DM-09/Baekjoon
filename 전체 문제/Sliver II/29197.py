import sys

def input(): return sys.stdin.readline().rstrip()

s = set()

for _ in range(int(input())):
    x, y = map(int, input().split())
    i, j = '+' if x > 0 else '-', '+' if y > 0 else '-'

    if x == 0: i = ''
    if y == 0: j == ''

    re = i + j + '0.0'

    if x != 0: re = i + j + str(y / x)
    s.add(re)

print(len(s))
