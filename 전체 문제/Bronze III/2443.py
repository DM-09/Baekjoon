n = int(input())

j = n * 2 - 1
for i in range(n):
    print(' ' * (i) + '*' * j)
    j -= 2
