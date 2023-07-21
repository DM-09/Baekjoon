while True:
    i = int(input())
    if i == 0: break

    page = [0 for _ in range(i)]

    want = input().split(',')
    for w in want:
        point = list(map(int, w.split('-')))

        if point[0] <= i:
            point.append(point[0])
            if point[1] > i: point[1] = i

            for p in range(point[0] - 1, point[1]):
                page[p] = 1

    print(sum(page))
