def m2a(s):
    m = 'abkdeghilmnoprstuwy'
    a = 'abcdefghijkmnopqrst'

    s = s.replace('ng', '!')

    for i in range(19): s = s.replace(m[i], a[i])
    return s.replace('!', 'l')

A = [input() for _ in range(int(input()))]

print(*sorted(A, key=lambda x: m2a(x)))
