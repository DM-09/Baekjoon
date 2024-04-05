n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

def Hfilp(t):
  new = []
  for i in list(t): new.append(i[::-1])
  return new

def Lrotate(t):
  new = [[] for _ in range(n)]
  start = n - 1
  
  for j in list(t):
    for i in range(len(j)):
      new[start+i].append(j.pop())
    start -= 1

  return new

def Rrotate(t):
  new = [[] for _ in range(n)]
  for j in range(n):
    for i in list(t):
      if i: new[-1-j].append(i.pop())
    new[-1-j] = new[-1-j][::-1]
  
  return new

def diff(a, b):
  r = 0
  for i in range(len(a)):
    for j in range(len(a[i])):
      if a[i][j] != b[i][j]: r += 1

  return r

a_copy = [[row.copy() for row in a] for _ in range(6)]



ans = min(diff(a_copy.pop(), b),
          diff(Hfilp(a_copy.pop()), b),
          diff(Lrotate(a_copy.pop()), b), 
          diff(Lrotate(Hfilp(a_copy.pop())), b),
          diff(Rrotate(a_copy.pop()), b),
          diff(Rrotate(Hfilp(a_copy.pop())), b))

print(ans)
