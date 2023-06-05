from collections import deque
import sys
q = deque()

for i in range(int(input())):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push': q.append(cmd[1])
    if cmd[0] == 'pop': print(-1 if len(q) == 0 else q.popleft())
    if cmd[0] == 'size': print(0 if len(q) == 0 else len(q))
    if cmd[0] == 'empty': print(1 if len(q) == 0 else 0)
    if cmd[0] == 'front': print(-1 if len(q) == 0 else q[0])
    if cmd[0] == 'back': print(-1 if len(q) == 0 else q[len(q) - 1])
