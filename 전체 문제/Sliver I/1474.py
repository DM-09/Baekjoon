n, m = map(int, input().split())
l = [input() for _ in range(n)]

length = sum([len(i) for i in l])
left = m - length
blank = n - 1

under = 0

while left > blank:
    left -= blank
    under += 1

over = m - length - under * blank
p = [l[0]]

s = '_' * under

for ind in range(n-1):
    i = l[ind+1]
    a = s + ('_' if over > 0 else "")

    if n-ind-1 <= over:
        p.append(a)
        p.append(i)
        continue

    if sorted([a, i])[0] == a: p.append(a); over -= 1
    else: p.append(s)
    p.append(i)

print(''.join(p))
