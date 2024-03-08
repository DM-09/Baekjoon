html = input().split('>')
l = []
for i in html:
  i += '>'
  if i.count('title="'):
    index1 = i.index('="')
    index2 = i.index('">')
    print('title : '+i[index1+2:index2])
    continue
  l.append(i)
  if i.count('</p>'):
    s = ''.join(l).replace('<', '>|')
    b = []
    for j in s.split('>'):
      if j == '' or j.count('|'): continue
      b.append(j)
    print(' '.join(''.join(b).split()))
    l = []
