N, M = map(int, input().split())
bas = []

for q in range(N): bas.append(0)

for e in range(M):
    i, j, k = map(int, input().split())
    for s in range(i, j + 1):
        bas[s - 1] = k

print(str(bas).replace(',', '').replace('[', '').replace(']', ''))
