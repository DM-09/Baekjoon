from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

l = deque()
last = []

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == '3':
        if len(l) != 0:
            if last[-1]: l.pop()
            else: l.popleft()
            last.pop()
    else:
        c, n = int(cmd[0]), cmd[1]
        if c == 1: l.append(n); last.append(1)
        else: l.appendleft(n); last.append(0)

l = ''.join(l)
print(0 if l == '' else l)
