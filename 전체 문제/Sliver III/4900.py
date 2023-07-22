while True:
    seg_num = ['063', '010', '093', '079', '106', '103', '119', '011', '127', '107']

    i, ii = input().replace('=', '').split('+'), 0
    num = [[], []]

    if i[0] == 'BYE': break

    for c in i:
        s = []
        for m in range(len(c)):
            s.append(c[m])
            if (m + 1) % 3 == 0:
                num[ii].append(str(seg_num.index(''.join(s))))
                s = []
        ii += 1

    new = int(''.join(num[0])) + int(''.join(num[1]))

    a = ''
    for w in str(new): a += seg_num[int(w)]
    print(f'{i[0]}+{i[1]}={a}')
