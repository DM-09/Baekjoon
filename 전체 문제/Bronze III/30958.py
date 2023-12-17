n = int(input())
s = input()

d = {}

for i in s:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        try: d[i] += 1
        except: d[i] = 1

print(sorted(d.items(), key=lambda x: -x[1])[0][1])
