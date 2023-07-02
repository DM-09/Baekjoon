l = []

N, M = input().split()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in A: l.append(i)
for i in B: l.append(i)

l = sorted(l)

print(*l)
