import re

s = input()
n, m, z = 0, 1, False

s = re.sub('hk|ho|hl|nj|np|nl|ml', '@', s)
s = re.sub('rt|sw|sg|fr|fa|fq|ft|fx|fv|fg|qt', '~', s)
s = re.sub('k|i|j|u|h|y|n|b|m|l|o|p|O|P', '#', s)
s = re.sub('r|s|e|f|a|q|t|d|w|c|z|x|v|g|Q|W|E|R|T', '!', s)

for i in s:
    n += 1
    if i in ['@', '~']: n += 1
    if m == 1:
        m = 2
        if i == '~': break
        if not z and i in ['@', '#']:
            if i == '@': n -= 1
            break
        if z and i != '!':
            m, z = 3, False
    elif m == 2:
        if i in ['!', '~']: break
        m = 3
    else:
        if i == '@': n -= 1
        if i in ['@', '#']: break
        z, m = True, 1
else: n = 0

print(n)
