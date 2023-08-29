n = int(input())
a = list(map(int, input().split()))

s = sorted(set(a), reverse=True)
d, ls, new = {}, len(s), []

for i in range(ls): d[s[i]] = ls - 1 - i
for i in a: new.append(d[i])

print(*new)
