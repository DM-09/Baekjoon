def t2n(num, base):
    tmp = '0123456789'
    q, r = divmod(num, base)
    return tmp[r] if q == 0 else t2n(q, base) + tmp[r]


inp = lambda: [*map(int, input().split())]

box = inp()
base = sum(box) % 10

for _ in range(int(input())):
    for i, eat in enumerate(inp()): box[i] -= eat

    num = sum(box)
    if base in [0, 1]: base = 10
    num = t2n(num, base)
    print(f'{num}7H')

    if num == '0': print('NULL')

    box2, al, s = [], 'HTCKG', 0
    for i in range(5): box2.append((-box[i], al[i]))

    for n, name in sorted(box2):
        if n == 0: break
        print(name, end='')
        s += 1
    if s != 0: print()

    base = sum(box) % 10
