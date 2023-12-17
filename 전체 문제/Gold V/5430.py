from collections import *
import sys
def input(): return sys.stdin.readline().rstrip()

for _ in range(int(input())):
    cmd = input()
    n = int(input())
    l = deque(eval(input()))
    re = 0

    for i in cmd:
        if i == 'R': re = not re
        else:
            if len(l) == 0: print('error'); break
            if re: l.pop()
            else: l.popleft()
    else:
        if re: l = list(l)[::-1]
        print(f'[{",".join(map(str, l))}]')
