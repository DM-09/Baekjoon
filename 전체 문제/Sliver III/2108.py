n = int(input())
a = [int(input()) for _ in range(n)]

div = n if n != 0 else 1

average = int(round(sum(a) / div, 0))
middle = sorted(a)[n // 2] if n != 0 else 0
range_ = abs(min(a) - max(a))

l = {}

for i in a:
    try: l[i] += 1
    except: l[i] = 1

l = sorted(l.items(), key=lambda x: (-x[1], x[0]))
ml = max(l, key=lambda x: x[1])[1]
many = l[0][0]

if n != 1:
    if l[0][1] == ml and l[1][1] == ml:
        many = l[1][0]

print(average, middle, many,  range_)
