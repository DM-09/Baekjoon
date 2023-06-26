for _ in range(int(input())):
    N, M = map(int, input().split())
    n = 0

    for i in range(N, M + 1):
        if str(i).find('0') != -1:
            n += str(i).count('0')

    print(n)
