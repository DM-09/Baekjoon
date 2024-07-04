def dpow(d: str, b: int):
  a = int(d.replace('.', ''))

  tail = len(d[d.index('.') + 1:])
  mul = str(a ** b)
  n = len(mul) - tail * b

  l = mul[:n]
  r = mul[n:]

  if d[0] == '0':
    l = '0'; r = mul
    r = '0' * (tail * b - len(r)) + r
  return l + '.' + r

def get(n, m):
  s = str(n) + '.'
  for _ in range(10):
    p = '0'
    for j in range(10):
      a = s + str(j)
      q = dpow(a, 3)
      w = str(m) + '.' + q.split('.')[1]

      q = '0' * (len(w) - len(q)) + q
      if q >= w: s += p; break
      p = str(j)
    else: s += '9'
  return s

for _ in range(int(input())):
  n = int(input())
  l = len(str(n)) // 3 + 1
  s = ['0'] * l

  for i in range(l):
    for j in range(10):
      s[i] = str(j)
      c = int(''.join(s)) ** 3
      if c > n:
        s[i] = str(j - 1); break
      elif c == n:
        break

  s = int(''.join(s))
  print(get(s, n))
