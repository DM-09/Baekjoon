while 1:
    N = int(input())
    if N == 0: break

    a = sorted([int(input()) for _ in range(N)])

    for i in range(len(a) - 1):
        if a[i + 1] - a[i] > 200:
            print('IMPOSSIBLE')
            break
    else:
        print('POSSIBLE' if 1442 - a[-1] < 100 else 'IMPOSSIBLE')
