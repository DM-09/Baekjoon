import re

s = input()

s = re.sub('rt|sw|sg|fr|fa|fq|ft|fx|fv|fg|qt', '&', s)
s = re.sub('hk|ho|hl|nj|np|nl|ml', '@', s)
s = re.sub('W|E|Q', '#', s)
s = re.sub('r|R|s|e|f|a|q|t|T|d|w|c|z|x|v|g', '!', s)
s = re.sub('k|o|i|O|j|p|u|P|h|y|n|b|m|l', '@', s)

mode, n = 0, 0

for i in s:
    if mode == 0:
        if i in '!#': mode = 1
        elif i == '@':
            n += 1
            mode = 2
    elif mode == 1:
        if i == '@': mode = 2
    elif mode == 2:
        if i in '!&': mode = 0

    if not i in '!@&#': mode = 0

print(n)
