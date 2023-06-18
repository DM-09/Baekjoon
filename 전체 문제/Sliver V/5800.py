for i in range(int(input())):
    l = list(map(int, input().split()))
    r = []

    del l[0]
    l.sort()

    for j in range(len(l)):
        try:
            r.append(abs(l[j] - l[j + 1]))
        except:
            break

    m1, m2 = max(l), min(l)

    print(f'Class {i + 1}')
    print(f'Max {m1}, Min {m2}, Largest gap {max(r)}')
