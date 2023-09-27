I, N, K = map(int, input().split())
ink_s = input()
stage = [list(input()) for _ in range(N)]
cmd = input()

x, y, ink, d = 0, 0, 0, 0
ss = ink_s + '#'

for i in range(len(stage)):
    l = stage[i]
    for j in range(len(l)):
        if l[j] == '@': x = i; y = j; break

def move(cmd):
    global stage, x, y, N, ss
    moves = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
    cur = moves[cmd]
    c = [x, y]
    stage[x][y] = '.'

    N -= 1

    x += cur[0]
    y += cur[1]

    if x < 0: x = c[0]
    if y < 0: y = c[1]
    if x > N: x = c[0]
    if y > N: y = c[1]

    if str(stage[x][y]) in ss: x = c[0]; y = c[1]
    stage[x][y] = '@'
    N += 1


def jump(color):
    global stage, x, y, ink, N, d

    for a in range(N):
       for b in range(N):
           if abs(x - a) + abs(y - b) <= ink and stage[a][b] in ss:
               stage[a][b] = color
    ink = 0
    d += 1
    if d == I: d = 0


for i in cmd:
    if i == 'J': jump(ink_s[d])
    elif i == 'j': ink += 1
    else: move(i)

for i in stage: print(''.join(i))
