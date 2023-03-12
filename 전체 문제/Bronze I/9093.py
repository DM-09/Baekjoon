N = int(input())

for i in range(N):
    inp = input().split()

    for c in range(len(inp)):
        inp[c] = inp[c][::-1]
    print(*inp)
