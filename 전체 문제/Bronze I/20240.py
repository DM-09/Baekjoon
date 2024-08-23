n = int(input())
l = None

for i in range(n):
  a = n - i ** 2
  if a < 0: break
  if (b := int(a ** .5)) ** 2 == a:
    l = [i, b]
    break

if not l: exit(print('Impossible'))

p, q = l
print(0, p)
print(q, 0)
print(p + q, q)
print(p, p+q)
