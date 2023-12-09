def frep(s : str, p : str):
    st, f, lf = [], list(p), len(p)
    a, n = 0, 0

    if p == '}{': a = 2
    if p in ['}}', '{{']: a = 1

    for i in s:
        st.append(i)
        if st[-lf:] == f:
            n += a
            for _ in range(lf): st.pop()
    return ''.join(st), n

a = 1
while 1:
    i, n = input(), 0
    if i[0] == '-': break

    for q in ['{}', '{{', '}}', '}{']:
        w, e = frep(i, q)
        i = w
        n += e

    print(f'{a}.', n)
    a += 1
