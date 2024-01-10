i = lambda: map(int, input().split())
a, b = i()
c, d = i()
e, f = i()

t = (c*f - c*b - a*f) - (d*e - d*a - b*e)

if t > 0: print(1)
elif t < 0: print(-1)
else: print(0)
