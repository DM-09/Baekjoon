def n_sum(s: str):
    l = []
    for i in s:
        if i.isdigit(): l.append(int(i))
    return sum(l)

l = [input() for _ in range(int(input()))]

print(*sorted(l, key= lambda x: (len(x), n_sum(x), x)))
