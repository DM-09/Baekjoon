n, m = map(int, input().split())

group = []
member = []

for _ in range(n):
    group.append(input())
    member.append(' '.join([input() for _ in range(int(input()))]))

for _ in range(m):
    q = input()
    mode = input()

    if mode == '0':
        for i in sorted(member[group.index(q)].split()):
            print(i)
    else:
        for i in range(len(member)):
            if q in member[i]: print(group[i])
