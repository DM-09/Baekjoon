def decimal_format(n, d):
    return float(f"{{:.{d}f}}".format(n))

a, b = map(int, input().split())
print(decimal_format(a * b / 2, 1))
