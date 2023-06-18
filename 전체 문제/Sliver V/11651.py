l = []

for i in range(int(input())):
    li = list(map(int, input().split()))
    l.append([li[1], li[0]])

for i in sorted(l):
    print(i[1], i[0])
