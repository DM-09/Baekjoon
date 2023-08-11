def t2n(num, base):
    tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q, r = divmod(num, base)
    return tmp[r] if q == 0 else t2n(q, base) + tmp[r]

for _ in range(int(input())):
    A, B = input().split()
    print(t2n(int(A, 2) + int(B, 2), 2))
