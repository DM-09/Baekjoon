d = 0

for i in range(4):
    by, num = input().split()
    if by[0] == 'S':
        d += 17 * int(num)
    else:
        d += 21 * int(num)

print(d)
