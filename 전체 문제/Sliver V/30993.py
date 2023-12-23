from math import factorial as f
n, a, b, c = map(int, input().split())
print((f(n) // (f(a) * f(n-a))) * (f(n-a) // (f(b) * f(n-b-a))))
