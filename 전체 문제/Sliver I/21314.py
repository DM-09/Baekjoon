s = input()

## MAX

c = 1
m = 0
v = [''] * len(s)

for i in range(len(s)):
  cur = s[i]
  if cur == 'K':
    c *= 5 * pow(10, m)
    v[i] = str(c)
    c = 1
    m = 0
  else: m += 1

if s[-1] == 'M': v[-1] = str('1'*m)
print(''.join(v))

## MIN

m = 0
v = [''] * len(s)

for i in range(len(s)):
  cur = s[i]
  if cur == 'K':
    if m > 0: v[i-1] = str(pow(10, m-1))
    v[i] = '5'
    m = 0
  else: m += 1
if m > 0: v[-1] = str(pow(10, m-1))
print(''.join(v))
