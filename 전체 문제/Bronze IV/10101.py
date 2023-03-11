s, c, r = int(input()), int(input()), int(input())
su = sum([s, c, r])

if su != 180:
    print('Error')
elif s == 60 and c == 60 and r == 60:
    print('Equilateral')
elif s == c or s == r or c == r:
    print('Isosceles')
else:
    print('Scalene')
