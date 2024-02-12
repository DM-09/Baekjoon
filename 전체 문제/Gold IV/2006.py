def parse(s):
  par = s.replace('+', ' ')
  atoms = {}
  mult, amult = 1, 1
  cur, b, pre, flag = '', '', '', 2

  for i in par+' A':
    if i.isdigit(): b += i; continue
    if cur == '' and b: mult = int(b); b = ''
    elif b: amult = int(b); b = ''

    if cur != '' and i.isupper() or i == ' ':
      atoms[cur] = mult * amult + atoms.get(cur, 0)
      cur = i
      amult = 1
      if i == ' ': mult = 1; b = ''; cur = ''
    else: cur += i

  return atoms

def diff(a, b, index):
  p = [f'Equation {index} is unbalanced.']
  s = set()
  for i in a: s.add(i)
  for i in b: s.add(i)

  for i in sorted(s):
    q, w = a.get(i, 0), b.get(i, 0)
    dif = abs(q - w)
    if dif == 0: continue
    if q < w: p.append(f'You have created {dif} atom{"s"if dif>1 else ""} of {i}.')
    if w < q: p.append(f'You have destroyed {dif} atom{"s"if dif>1 else ""} of {i}.')

  if len(p) > 1: return p+['']
  return [f'Equation {index} is balanced.']

index = 1
while 1:
  inp = input().replace(' ', '')
  if inp == '#': break

  inp = inp.split('=')
  for i in diff(parse(inp[0]), parse(inp[1]), index): print(i)
  index += 1
