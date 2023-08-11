def Camel(s :str):
    l = s.split('_')
    r, ind = '', 0

    for i in l:
        if ind == 0: r += i[0].lower() + i[1:]; ind = 1
        else: r += i[0].upper() + i[1:]
    return r

def Snake(s :str):
    r = ''
    s = s[0].lower() + s[1:]

    for i in s:
        if i.isupper(): r += '_' + i.lower()
        else: r += i.lower()
    return r

def Pascal(s : str):
    l = s.split('_')
    r = ''

    for i in l: r += i[0].upper() + i[1:]
    return r

i, word = input().split()

print(Camel(word))
print(Snake(word))
print(Pascal(word))
