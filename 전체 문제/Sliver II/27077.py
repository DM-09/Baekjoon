Ko = list(map(int, input().split()))
Ur = list(map(int, input().split()))
Gh = list(map(int, input().split()))
Po = list(map(int, input().split()))

Ko.append('K')
Ur.append('U')
Gh.append('G')
Po.append('P')

k, p = 0, 0
u, g = 0, 0

def f(K, U, G, P, k, u, g, p):
    if k == p: K[2] += 1; P[2] += 1
    elif k > p: K[2] += 3
    else: P[2] += 3

    if u == g: U[2] += 1; G[2] += 1
    elif u > g: U[2] += 3
    else: G[2] += 3

    K[0] += k
    K[1] += p
    P[0] += p
    P[1] += k

    U[0] += u
    U[1] += g
    G[0] += g
    G[1] += u

    team = [K, U, G, P]
    s = 'PUGK'
    team.sort(key=lambda x: (-x[2], -(x[0] - x[1]), -x[1], s.index(x[3])))

    for i in range(4):
        cur = team[i]
        if i == 2: return 'unhappy'
        if cur[3] == 'K': return 'cry'

print(f(Ko, Ur, Gh, Po, 0, 0, 0, 0))


for _ in range(int(input())):
    w = input()[0]

    if w == 'k': k += 1
    if w == 'u': u += 1
    if w == 'g': g += 1
    if w == 'p': p += 1

    print(f(list(Ko), list(Ur), list(Gh), list(Po), k, u, g, p))
