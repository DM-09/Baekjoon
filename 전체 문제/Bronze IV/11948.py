s, h = [], []
for i in range(6):
    if i < 4:
        s.append(int(input()))
    else:
        h.append(int(input()))

s.sort(); h.sort()
del s[0]; del h[0]
print(sum(s) + sum(h))
