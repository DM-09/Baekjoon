a, b = map(int, input().split())
n = a / 100 * b

if a - n >= 100:
    print(0)
else:
    print(1)
