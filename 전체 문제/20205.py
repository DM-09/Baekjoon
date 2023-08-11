N, M = map(int, input().split())

for _ in range(N):
    i, r = input().split(), ''

    for j in i: r += (j + ' ') * M
    for _ in range(M): print(r)
