n = int(input())
a = sorted(list(map(int, input().split())))
p = a[0] * a[1]

l = [a[0] + a[1]]

for i in range(len(a) - 2):
    ll, cur = l[i], a[i + 2]
    l.append(ll + cur)
    p += ll * cur

print(p)
