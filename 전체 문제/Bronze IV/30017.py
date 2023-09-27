a, b = map(int, input().split())
s = (a - 1 if b >= a - 1 else b)
print(s + s + 1)
