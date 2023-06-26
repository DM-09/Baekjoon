o = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
r = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

s = ''

for i in input():
    if o.find(i) == -1:
        s += i
    else:
        s += r[o.index(i)]

print(s)
