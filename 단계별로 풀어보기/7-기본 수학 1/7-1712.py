A, B, C = list(map(int, input().split()))
mi = C - B
if mi <= 0:
    print(-1)
else:
    print(A // mi + 1)
