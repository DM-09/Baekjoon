N = int(input())
cs = 1

for i in range(N):
    print(' ' * (N - i - 1) + "*" * cs)
    cs += 2

cs -= 2

for i in range(N):
    cs -= 2
    print(' ' * (i + 1) + "*" * cs)
