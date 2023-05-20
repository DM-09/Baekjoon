i, l = int(input()), sum(list(map(int, input().split())))
n = (i - 1) * 8 + l

print(n // 24, n % 24)
