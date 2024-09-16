a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

t = a + b*2 + c*3
t2 = x + y*2 + z*3

if t == t2: print(0)
else: print(1+(t<t2))
