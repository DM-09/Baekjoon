name = input()
l = []

for _ in range(int(input())):
    team = input()

    L = name.count('L') + team.count('L')
    O = name.count('O') + team.count('O')
    V = name.count('V') + team.count('V')
    E = name.count('E') + team.count('E')

    formula = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    l.append([formula, team])

l.sort()
m, na = -1, ''

for i in l:
    if i[0] > m:
        m, na = i[0], i[1]

print(na)
