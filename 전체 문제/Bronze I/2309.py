l = [int(input()) for i in range(9)]
b = False

for i in range(9):
    if b: break
    for j in range(9):
        if i != j:
            n = sum(l) - l[i] - l[j]

            if n == 100:
                del l[i], l[j - 1]
                print(*sorted(l))
                b = True; break
