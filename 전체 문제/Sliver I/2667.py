from collections import deque

n = int(input())
table = []
todo = []

for i in range(n):
    l = input()
    for j in range(len(l)):
        if l[j] == '1': todo.append([j, i])

while todo:
    cur = todo[0]
    count = 1
    todo.remove(cur)

    box = deque([(cur[0], cur[1])])
    while box:
        c = box.popleft()
        for i in [[c[0], c[1] - 1],
                  [c[0] + 1, c[1]],
                  [c[0] - 1, c[1]],
                  [c[0], c[1] + 1]]:
            if i in todo:
                box.append(i)
                todo.remove(i)
                count += 1

    table.append(count)

print(len(table))
print(*sorted(table))
