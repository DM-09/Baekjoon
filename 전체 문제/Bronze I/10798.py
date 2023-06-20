l = [input() for _ in range(5)]
s = ''

for i in range(15):
    try:
        for j in range(5):
            if len(l[j]) - 1 >= i:
                s += l[j][i]
    except:
        pass
print(s)
