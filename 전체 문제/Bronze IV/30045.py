n = 0

for _ in range(int(input())):
    s = input()
    f = s.find('OI')
    f2 = s.find('01')

    if f != -1 or f2 != -1: n += 1

print(n)
