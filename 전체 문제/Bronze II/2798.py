n, m = map(int, input().split())
a = list(map(int, input().split()))
c = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                s = a[i] + a[j] + a[k]
                o = c
                if s > c: c = s
                if c > m: c = o

print(c)
