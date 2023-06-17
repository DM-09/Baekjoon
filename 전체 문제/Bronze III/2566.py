l = [input().split() for j in range(9)]
m = 0
x, y = 1, 1

for i in range(len(l)):
    for j in range(len(l[i])):
        if int(l[i][j]) > m:
            m = int(l[i][j])
            x, y = i + 1, j + 1

print(m)
print(x, y)
