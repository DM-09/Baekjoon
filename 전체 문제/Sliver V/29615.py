m, n = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

v = n

for i in range(n):
    if a[i] in f: v -= 1

print(v)
