def f(n):
  l = ['1']
  s = []

  for _ in range(20):
    for j in range(len(l)):
      a = l[j]
      s.append(a + '0')
      s.append(a + '1')

    for i in s:
      if int(i) % n == 0:
        return i

    l = list(s)
    s = []

a = {}
for i in range(1, 201): a[i] = f(i)

while 1:
  n = int(input())
  if n == 0: break
  print(a[n])
