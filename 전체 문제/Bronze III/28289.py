Sw, Im, Ai, fr = 0, 0, 0, 0

for _ in range(int(input())):
    G, C, N = map(int, input().split())
    if G == 1:
        fr += 1
    else:
        if C in [1, 2]:
            Sw += 1
        elif C == 3:
            Im += 1
        else:
            Ai += 1

print(Sw, Im, Ai, fr)
