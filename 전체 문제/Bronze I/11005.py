def t2n(num, base):
    tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q, r = divmod(num, base)
    return tmp[r] if q == 0 else t2n(q, base) + tmp[r]

A, B = map(int, input().split())

print(t2n(A, B))
