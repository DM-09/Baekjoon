def t2n(num, base):
    tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q, r = divmod(num, base)
    return tmp[r] if q == 0 else t2n(q, base) + tmp[r]

print(int(t2n(int(input()), 2)[::-1], 2))
