from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    cabbage_list = []
    find = {}
    num = 0

    for _ in range(k):
        a, b = map(int, input().split())
        cabbage_list.append([a, b])
        find[(a, b)] = 1

    while cabbage_list:
        tu = cabbage_list[0]
        todo = deque([(tu[0], tu[1])])
        num += 1

        cabbage_list.remove(tu)

        while todo:
            cur = todo.popleft()
            xc, yc = cur[0], cur[1]
            for i in [[xc, yc - 1], [xc, yc + 1], [xc - 1, yc], [xc + 1, yc]]:
                if i in cabbage_list: todo.append(i); cabbage_list.remove(i)

    print(num)
