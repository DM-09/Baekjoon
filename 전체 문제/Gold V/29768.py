n, k = map(int, input().split())
al = 'bcdefghijklmnopqrstuvwxyz'

print('a' * (n - k + 1) + al[:k - 1])
