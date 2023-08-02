names = []
values = {}

for _ in range(int(input())):
    i = input().split()
    n = i[0]
    names.append(n)

    values[n] = (-int(i[1]), int(i[2]), -int(i[3]), i[0])

print(*sorted(names, key=lambda x: values[x]))
