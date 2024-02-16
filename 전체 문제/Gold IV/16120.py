def frep(s, f: str):
  st, f, lf = [], list(f), len(f)
  flag = 0
  for i in s:
    st.append(i)
    if st[-lf:] == f:
      for _ in range(lf): st.pop()
      st.append('P')
      if st == ['P']: flag = 1
  if s == 'P': return 1
  if flag and st == ['P']: return 1
  return 0

print('PPAP' if frep(input(), 'PPAP') else 'NP')
