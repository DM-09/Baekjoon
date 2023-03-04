def printer(l):
    for i in l:
        print(*i)


N, M, K = map(int, input().split())
a = N + M - 1

if a <= K:
    print('YES')
    l = [[i for i in range(1 + j, M + 1 + j)] for j in range(N)]
    printer(l)
else:
    print('NO')
