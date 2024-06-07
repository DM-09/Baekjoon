n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

def get(l):
  box = 0

  for i in l:
    i = [0] + i + [0]
    for j in range(len(i)-1):
      box += abs(i[j]-i[j+1])
      
  return box

p = []

for i in range(m):
  box = []
  for j in range(n):
    box.append(l[j][i])
  p.append(box)
  
print(get(l) + get(p) + m * n * 2) 
