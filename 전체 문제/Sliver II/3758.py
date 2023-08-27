for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    l = [[[0] * k, 0, 0, i + 1] for i in range(n)]

    for q in range(m):
        i, j, s = map(int, input().split())
        team = l[i - 1]

        if team[0][j - 1] < s: team[0][j - 1] = s
        team[1] += 1
        team[2] = q + 1

    my = l[t - 1]
    l = sorted(l, key=lambda x: (-sum(x[0]), x[1], x[2]))

    print(l.index(my) + 1)
