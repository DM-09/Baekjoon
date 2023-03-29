N = int(input())
p, d = 0, 0

for i in range(N):
    r = input()
    if r == 'D':
        d += 1
    else:
        p += 1
    if abs(p - d) == 2:
        break

print(f'{d}:{p}')
