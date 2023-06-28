s, e = input(), ''
ss = ['.', '.', '#', '.', '.']
p = True

def more():
    ss[0] += '.'
    ss[1] += '.'
    ss[2] += '#'
    ss[3] += '.'
    ss[4] += '.'

for i in range(len(s)):
    if i != 0 and (i + 1) % 3 != 0 and p:
        more()

    if (i + 1) % 3 == 0:
        ss[0] += '..*..'
        ss[1] += '.*.*.'
        ss[2] += f'*.{s[i]}.*'
        ss[3] += '.*.*.'
        ss[4] += '..*..'

        p = False
    else:
        ss[0] += '.#.'
        ss[1] += '#.#'
        ss[2] += f'.{s[i]}.'
        ss[3] += '#.#'
        ss[4] += '.#.'

        p = True

if p: more()
for i in ss: print(i)
