N, M = map(int, input().split())
bas = []

for s in range(1, N + 1): bas.append(s)

for q in range(M):
    i, j = map(int, input().split())
    inum = bas[i - 1]
    jnum = bas[j - 1]
    bas[i - 1] = jnum
    bas[j - 1] = inum

print(str(bas).replace(',', '').replace('[', '').replace(']', ''))
