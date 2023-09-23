n, m, k = map(int, input().split())
a = n - m * k
print(a if a > 0 else 0, a + m - 1)
