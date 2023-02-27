a, b = map(int, input().split())
n = a - b

if n < 0:
    print(n * -1)
else:
    print(n)
