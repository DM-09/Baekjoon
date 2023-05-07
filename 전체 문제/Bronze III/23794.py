n = int(input())
m = 2 + n

print('@' * m)
for _ in range(n): print('@' + (' ' * n) + '@')
print('@' * m)
