import sys
stack = []

for i in range(int(input())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push': stack.append(cmd[1])
    if cmd[0] == 'pop': print(-1 if len(stack) == 0 else stack.pop())
    if cmd[0] == 'size': print(len(stack))
    if cmd[0] == 'empty': print(1 if len(stack) == 0 else 0)
    if cmd[0] == 'top': print(-1 if len(stack) == 0 else stack[len(stack) - 1])
