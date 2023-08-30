d, n = {}, 0

while 1:
    try:
        i = input()
        try: d[i] += 1
        except: d[i] = 1

        n += 1

    except: break

d = sorted(d.items())

for i, j in d:
    print(i, '{:.4f}'.format((j / n) * 100))
