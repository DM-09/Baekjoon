n = int(input())

j = 1
m = n * 2
for i in range(n - 1):
    print('*' * j + ' ' * (m - j * 2) + '*' * j)
    j += 1
for i in range(n):
    print('*' * j + ' ' * (m - j * 2) + '*' * j)
    j -= 1
