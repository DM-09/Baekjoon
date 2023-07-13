l = dict()

for _ in range(int(input())):
    name = input()

    try:
        l[name] += 1
    except:
        l[name] = 1

m = []
mv = max(l.values())

for k, v in sorted(l.items()):
    if v == mv: m.append(k)

print(sorted(m)[0])
