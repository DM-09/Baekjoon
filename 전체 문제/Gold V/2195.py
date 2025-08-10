s = input()
p = input()

cnt = 0
ind = 0

while ind < len(p):
  for i in range(len(p)-ind):
    cur = p[ind:len(p)-i]
    if s.find(cur) > -1 and cur != '':
      ind += len(cur)
      cnt += 1

print(cnt)
