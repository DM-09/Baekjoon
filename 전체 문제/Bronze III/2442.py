n = int(input())

j = 1
for i in range(n):
    print(' ' * (n - i - 1) + '*' * j)
    j += 2
