l = []

for _ in range(int(input())):
    a = list(map(int, input().split()))

    run = max(a.pop(0), a.pop(0))
    m2 = sum(sorted(a)[-2:])
    l.append(run + m2)

print(max(l))
