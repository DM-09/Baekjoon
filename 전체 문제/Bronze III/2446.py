n = int(input())

j = n * 2 - 1
for i in range(n - 1):
    print(' ' * (i) + '*' * j)
    j -= 2
for i in range(n):
    print(' ' * (n - i - 1) + '*' * j)
    j += 2
