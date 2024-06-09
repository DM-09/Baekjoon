n = int(input())
s = ' '.join([input() for _ in [0] * n])

def long(l):
  a, w, p = 1, 0, ''
  for i in l.split():
    if i != p: w = max(w, a); a = 1
    else: a += 1
    p = i
  return max(w, a)

m = 0
for i in set(s.split()): m = max(m, long(s.replace(i, '')))
print(m)
