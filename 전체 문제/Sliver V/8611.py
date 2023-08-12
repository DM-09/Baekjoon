import sys
sys.setrecursionlimit(10**6)

def is_ok(s):
    if s == s[::-1]: return True
    return False

def n2n(num, base, base2, b=False):
    tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num2 = num if b else int(num, base)
    q, r = divmod(num2, base2)
    return tmp[r] if q == 0 else n2n(q, 0, base2, True) + tmp[r]
    
n = int(input())
c = 0

for i in range(1, 10):
    s = n2n(str(n), 10, i + 1)
    if is_ok(s):
        c += 1
        print(i + 1, s)

if c == 0: print('NIE')
