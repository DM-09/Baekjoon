N = int(input())
l = set()

for i in range(N):
    l.add(input())

l = list(l)
l = sorted(l, key=lambda x: (len(x), x))

for i in l:
    print(i)
