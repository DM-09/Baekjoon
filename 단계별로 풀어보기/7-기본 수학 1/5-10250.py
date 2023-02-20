T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    w = N // H + 1

    if (h := N % H) == 0:
        h = H
        w = N // H
    else:
        w = N // H + 1

    if w < 10:
        w = '0' + str(w)

    print(str(h) + str(w))
