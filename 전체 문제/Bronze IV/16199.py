y, m, d = map(int, input().split())
y1, m1, d1 = map(int, input().split())

yy = y1 - y

if m1 > m or m1 == m and d1 >= d:
    print(yy)
else:
    print(yy - 1)

print(yy + 1)
print(yy)
