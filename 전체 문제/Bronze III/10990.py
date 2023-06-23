N = int(input())

if N == 1:
    print('*')
else:
    b = 1
    print(' ' * (N - 1) + '*')

    for i in range(N - 1):
        print(' ' * (N - i - 2) + '*' + ' ' * b + '*')
        b += 2
