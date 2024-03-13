def frep(s: str, f: str):
  st, f, lf = [], list(f), len(f)
  l = [1] * len(s)
  for i in range(len(s)):
    st.append([s[i], i])
    a = []
    for b in st[-2:]: a.append(b[0])
    if a == f:
      for _ in range(lf): st.pop()

  for i in st: l[i[1]] = 0
  return l

n = int(input())
s = input()
m = 0
a = 0

for i in frep(s, '()'):
  if i: a += 1
  else: m = max(m, a); a = 0

print(max(m, a))
