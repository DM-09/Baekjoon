l = []

for i in range(500):
    for c in range(i + 1):
        l.append(i + 1)

a, b = map(int, input().split())
print(sum(l[a - 1:b]))
