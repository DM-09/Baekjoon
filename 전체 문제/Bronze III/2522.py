n = int(input())

c, b = 1, n - 1
for i in range(n - 1):
    print(' ' * b  + '*' * c)
    b -= 1
    c += 1
for i in range(n):
    print(' ' * b + '*' * c)
    b += 1
    c -= 1
