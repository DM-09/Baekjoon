table = [ ['.' for _ in range(20)] for _ in range(10)]
s = 'ABCDEFGHIJ'

for _ in range(int(input())):
    sit = input()
    a, b = '', ''

    for i in sit:
        if i.isdigit(): b += i
        else: a += i

    table[s.index(a)][int(b)-1] = 'o'

for i in table: print(''.join(i))
