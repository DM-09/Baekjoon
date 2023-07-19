import math

a, b = map(int, input().split())
print(int(b * math.log10(a)) + 1)
