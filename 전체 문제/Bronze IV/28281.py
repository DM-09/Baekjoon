N, X = map(int, input().split())
A = list(map(int, input().split()))
l = []

for i in range(N - 1):
    l.append(A[i] * X + A[i + 1] * X)

print(min(l))
