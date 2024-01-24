from collections import deque

n = int(input())
R, G, B = [], [], []
p, r = 0, 0

for i in range(n):
    inp = input()
    for j in range(n):
        if inp[j] == 'R': R.append([i, j])
        elif inp[j] == 'G': G.append([i, j])
        else: B.append([i, j])

for m in [[R,'R'], [G,'G'], [B,'B'], [R+G,'RG']]:
    b, f = m
    while b:
        x, y = b[0][0], b[0][1]
        todo = deque([(x, y)])
        if f != 'RG': p += 1
        if f in ['RG','B']: r += 1
        b.remove([x, y])

        while todo:
            c = todo.popleft()
            x, y = c[0], c[1]
            for i in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if i in b: todo.append(i); b.remove(i)
print(p, r)
