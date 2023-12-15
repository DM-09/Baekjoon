h, w = map(int, input().split())
pic = [input() for _ in range(h)]
n = 0

for a in pic:
    f = 0
    for i in a:
        if f == 2: f = 0
        if i !='.': f += 1

        if f: n += 1
        if f and i == '.': n += 1

print(n // 2)
