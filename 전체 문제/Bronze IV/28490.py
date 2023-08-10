l = []

for _ in range(int(input())):
    i, j = map(int, input().split())
    l.append(i * j)

print(max(l))
