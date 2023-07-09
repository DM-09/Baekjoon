N = int(input())
BN = 1
n = N - 2

for _ in range(n): BN += 2

print('*' * N + ' ' * BN + '*' * N)

for i in range(n):
    BN -= 2
    print(' ' * (i + 1) + '*' + ' ' * n + '*' + ' ' * BN + '*' + ' ' * n + '*')

print(' ' * (N - 1) + '*' + ' ' * n + '*' + ' ' * n + '*')

for i in range(n):
    print(' ' * (N - i - 2) + '*' + ' ' * n + '*' + ' ' * BN + '*' + ' ' * n + '*')
    BN += 2

print('*' * N + ' ' * BN + '*' * N)
