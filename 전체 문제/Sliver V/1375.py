l = ['0', '1', '2', '3', '4', '5', '7', '8', '9', '9']
n = 1
inp = input()

for i in inp:
    if i == '6': i = '9'

    if i in l:
        l.remove(i)
    else:
        n += 1
        for j in range(10):
            s = str(j) if j != 6 else '9'
            l.append(s)
        l.remove(i)
print(n)
