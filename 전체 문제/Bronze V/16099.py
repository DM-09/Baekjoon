for i in range(int(input())):
    u, r, u1, r1 = map(int, input().split())
    n, n1 = u * r, u1 * r1
    if n > n1:
        print('TelecomParisTech')
    elif n < n1:
        print('Eurecom')
    else:
        print('Tie')
