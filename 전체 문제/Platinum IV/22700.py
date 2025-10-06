n, m = map(int, input().split())
nxt = [n, m]
 
while 1:
 n, m = nxt
 party = []
 ep = []
 pn = dict()
 avote = 0
 if n+m == 0: break
 
 for i in range(m):
  name, c, v = input().split()
  c, v = int(c), int(v)
  party.append([name, v, i, [input() for _ in range(c)]])
  ep.append(dict())
  pn[name] = i
  avote += v
 
 while 1:
  a = list(map(int, input().split()))
  l = []
  if len(a) == 2:
   nxt = a
   break
  for _ in range(a[0]):
   name, pa, vo = input().split()
   l.append([name, pa, int(vo)])

  l.sort(key=lambda x: -x[-1])
  q = l[0]
  ep[pn[q[1]]][q[0]] = 1
  
 np = []
 nb = []
 cav = 0
 sn = 0
 
 for i in party:
  t = len(ep[i[2]])
  if i[1]/avote*100 >= 5 or t > 2:
   cav += i[1]
   nb.append([0, i[0], i[2], i[1], 0, 0])
 
 for i in range(len(nb)):
  box = nb[i]
  t = len(ep[box[2]])
  num = n*(box[3]/cav)
  sn += int(num)
  box[0] = num
  box[4] = num - t < 0
  box[5] = t
  np.append(box)
   
 sn = n - sn
 o = 0
 
 for i in np:
  for j in range(int(i[0]-i[5])):
   k = 0
   box = party[i[2]]
   while k < len(box[3]):
    cur = box[3][k]
    if ep[i[2]].get(cur, 0): k += 1
    else:
     ep[i[2]][cur] = 1
     break
  np[o][0] -= int(np[o][0])
  o += 1
 
 np.sort(key=lambda x: (-x[0], -x[3]))

 for j in range(sn):
  i = np[j]
  k = 0
  box = party[i[2]]
  if i[4]: continue
  while k < len(box[3]):
   cur = box[3][k]
   if ep[i[2]].get(cur, 0): k += 1
   else:
    ep[i[2]][cur] = 1
    break

 qu = []
 for i in ep: qu.extend([j for j in i])
 print('\n'.join(sorted(qu)))
 print()
