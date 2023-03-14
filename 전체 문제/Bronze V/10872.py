N = int(input()); a = 1

for i in range(1, N):
    a += a * (N - i)

print(a)
