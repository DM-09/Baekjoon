n, p, s = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F'], \
          [4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0], 0

m, t = input(), 0

for i in range(9):
    c = n[i]
    co = m.count(c)

    s += p[i] * co
    t += co
    m = m.replace(c, '')

print(s / t)
