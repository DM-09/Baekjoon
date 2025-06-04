l = list(map(int, input().split()))
l.sort()
a = {'A': l[0], 'B': l[1], 'C': l[2]}
n = []
for i in input(): n.append(str(a[i]))
print(*n)
