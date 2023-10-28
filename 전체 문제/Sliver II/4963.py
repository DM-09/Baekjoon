from collections import deque

while True:
    m, n = map(int, input().split())
    if (m == 0 and n == 0):
        break
    cabbage_list = []
    curr_map = []

    for i in range(n):
        curr = list(map(int, input().split()))
        for j in range(len(curr)):
            if curr[j] == 1:
                cabbage_list.append([j, i])

    worm = 0
    while cabbage_list:
        curr_c = cabbage_list[0]
        worm += 1
        cabbage_list.remove(curr_c)
        to_check = deque([(curr_c[0], curr_c[1])])
        while to_check:
            c = to_check.popleft()
            for adj_c in [[c[0] + 1, c[1]],
                          [c[0] - 1, c[1]],
                          [c[0], c[1] + 1],
                          [c[0], c[1] - 1],
                          [c[0] + 1, c[1] + 1],
                          [c[0] + 1, c[1] - 1],
                          [c[0] - 1, c[1] + 1],
                          [c[0] - 1, c[1] - 1]]:
                if adj_c in cabbage_list:
                    to_check.append(adj_c)
                    cabbage_list.remove(adj_c)

    print(worm)

