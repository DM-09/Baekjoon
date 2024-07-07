n, a = map(int, input().split())
mod = 10 ** 9 + 7
p=lambda a, b: pow(a, b, mod)
print(((n-1) * n * (p(n,a) - p(n-1, a)) + n * p(n-1, a)) % mod)
