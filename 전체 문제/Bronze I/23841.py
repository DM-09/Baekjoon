N, M = map(int, input().split())

for _ in range(N):
    inp = list(input())
    for i in range(M // 2):
        w = inp[i]
        r = M - i - 1
        if w != '.':
            inp[r] = w
        elif inp[r] != '.':
            inp[i] = inp[r]
    print(str(inp).replace('[', '').replace(']', '').replace(' ', '').replace("'", '').replace(',', ''))
