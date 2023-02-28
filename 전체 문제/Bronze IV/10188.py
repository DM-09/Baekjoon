N = int(input())
l = []

for i in range(N):
    l.append(list(map(int, input().split())))

for e in range(len(l)):
    for c in range(l[e][1]):
        print('X' * l[e][0])
    if e != len(l) - 1:
        print()
