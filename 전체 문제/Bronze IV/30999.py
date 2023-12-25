n, m = map(int, input().split())
a = 0
for _ in range(n):
    s = input()
    if s.count('O') > s.count('X'): a += 1

print(a)
