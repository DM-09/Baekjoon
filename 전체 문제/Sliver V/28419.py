def solve(a, l):
    i, E, O = 0, 0, 0

    for e in a:
        if i % 2 == 0: E += e
        else: O += e
        i += 1

    if l == 3 and E > O: return -1
    return abs(E - O)

N = int(input())
A = list(map(int, input().split()))

print(solve(A, N))
