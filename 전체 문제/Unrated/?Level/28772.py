i = input().split()
l = []

for j in i:
    if j[0] == '#' and j.count('#') == 1 and len(j) > 1: l.append(j)

print(len(set(l)))
for i in set(l): print(i, l.count(i))
