while True:
    n, a, w = input().split()
    if n == '#' and a == '0' and w == '0':
        break
    s = 'Junior'
    a, w = int(a), int(w)
    if a > 17 or w >= 80:
        s = 'Senior'
    print(f'{n} {s}')
