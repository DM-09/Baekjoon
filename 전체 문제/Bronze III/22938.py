x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

dx, dy = abs(x1-x2), abs(y1-y2)
if (r1+r2) > (dx ** 2 + dy ** 2) **.5: print("YES")
else: print('NO')
