N, M = map(int, input().split())
bas = []

for q in range(1, N + 1): bas.append(q)

for w in range(M):
    i, j = map(int, input().split())
    bas[i - 1:j] = list(reversed(bas[i - 1:j]))

print(str(bas).replace(',', '').replace('[', '').replace(']', ''))
