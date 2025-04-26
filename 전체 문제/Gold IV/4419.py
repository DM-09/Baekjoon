n = int(input())
candi = [[input(), i] for i in range(n)]
vote = []

while 1:
  try: vote.append(' '+input()+' ')
  except: break

def pnt(p): print('\n'.join([i[0] for i in sorted(p, key=lambda x: x[1])]))

remove = dict()

for _ in range(n-1):
  v = [j.split()[0] for j in vote]
  r = [[0, str(a), 0] for a in range(n+1)]

  for j in v: r[int(j)][0] += 1
  for i in range(len(r)): r[i][2] = r[i][0] / len(v)

  r.sort()
  _, *r = r

  if r[-1][2] >= 0.5:
    p = [candi[int(r[-1][1])-1]]
    if len(r) >= 2 and r[-2][2] >= 0.5:
      p.append(candi[int(r[-2][1])-1])
    pnt(p)
    break

  s = set()
  p = []
  for a, id, rate in r:
    if remove.get(id, 0): continue
    p.append(candi[int(id)-1])
    s.add(rate)

  if len(s) == 1: exit(pnt(p))

  m = r[0][0]

  for q, w, e in r:
    if not remove.get(w, 0):
      m = q
      break

  for q, w, e in r:
    if q == m:
      for i in range(len(vote)):
        vote[i] = vote[i].replace(' '+w+' ', ' ')
      remove[w] = 1
