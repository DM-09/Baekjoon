n = int(input())
al = {}

num = 1
for i in range(65, 91):
  al[chr(i)] = num
  al[chr(i).lower()] = num + 1
  num += 2

def parse(s):
  l = []
  numl = []
  is_pre_n = False
  for i in s:
    if i.isnumeric():
      numl.append(i)
      is_pre_n = True
    else:
      if is_pre_n and numl:
        l.append(('n', int(''.join(numl)), len(numl)))
        numl = []
      l.append(('z', al[i]))
      is_pre_n = False

  if numl: l.append(('n', int(''.join(numl)), len(numl)))
  return [(s,)] + l

for i in sorted([parse(input()) for _ in range(n)], key=lambda x: x[1:]): print(i[0][0])
