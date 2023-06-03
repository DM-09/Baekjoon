from collections import deque
import sys

d = deque()

for i in range(int(input())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front': d.appendleft(cmd[1])
    if cmd[0] == 'push_back': d.append(cmd[1])
    if cmd[0] == 'pop_front': print(-1 if len(d) == 0 else d.popleft())
    if cmd[0] == 'pop_back': print(-1 if len(d) == 0 else d.pop())
    if cmd[0] == 'size': print(len(d))
    if cmd[0] == 'empty': print(1 if len(d) == 0 else 0)
    if cmd[0] == 'front': print(-1 if len(d) == 0 else d[0])
    if cmd[0] == 'back': print(-1 if len(d) == 0 else d[len(d) - 1])
