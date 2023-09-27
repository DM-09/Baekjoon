n = int(input())
sub = input().split()
m = list(map(int, input().split()))
nsub = input().split()
k = int(input())
mar = input().split()
ss = int(input())
s = input().split()


def n_sub(s, sub, mar):
    l = []
    for i in sub:
        l = []
        if not i in mar:
            for j in s:
                l.append(' '.join(j.split(i)))

            s = ''.join(' '.join(l)).split()
    return s

for i in sub:
    l = []
    if not i in mar:
        for j in s:
            l.append(' '.join(j.split(i)))

        s = ''.join(' '.join(l)).split()

l = []
for i in s: l += n_sub(i.split(), nsub, mar)
print(*l)
