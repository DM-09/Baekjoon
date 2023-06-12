l = [int(input()) for _ in range(8)]
m = []
ind = []

for i in range(5):
    max_n = max(l)
    index = l.index(max_n)

    m.append(max_n)
    ind.append(str(index + 1))
    l[index] = -1

ind.sort()

print(sum(m))
print(' '.join(ind))
