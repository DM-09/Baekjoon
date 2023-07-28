def c2a(s: str):
    c, p, a = 'mnoprstuvz', '$%^&*()_+=', 'noqrstuvwx'

    s = s.replace('nj', '@').replace('lj', '!')

    for i in range(10): s = s.replace(c[i], p[i])
    for i in range(10): s = s.replace(p[i], a[i])

    return s.replace('@', 'p').replace('!', 'm')


print(*sorted([input() for _ in range(int(input()))], key=lambda x: c2a(x)))
