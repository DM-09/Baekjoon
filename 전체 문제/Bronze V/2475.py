n = list(map(int, input().split()))
nn = 0
for i in range(len(n)):
    nn += n[i] ** 2
print(nn % 10)
