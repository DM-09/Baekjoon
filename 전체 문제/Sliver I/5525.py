def build(s):
  n = len(s)
  f = [0] * n
  i = 0
  for j in range(1, n):
    while i > 0 and s[i] != s[j]: i = f[i-1]
    if s[i] == s[j]: i += 1; f[j] = i
  return f

def kmp(t, p, f):
  i = 0
  cnt = 0
  for j in range(len(t)):
    while i > 0 and p[i] != t[j]:
      i = f[i-1]
    if p[i] == t[j]:
      i += 1
      if i == len(p):
        cnt += 1
        i = f[i-1]
  return cnt

n = int(input())
l = int(input())
s = input()

p = ''.join(['IO' for _ in range(n)]+['I'])
print(kmp(s, p, build(p)))
