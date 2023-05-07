st, b = list(input()), list(reversed(input()))

bomb_length = len(b)
curr = []
while st:
  curr.append(st.pop())
  if curr[-bomb_length:] == b:
    for _ in range(bomb_length):
      curr.pop()
    
if len(curr) == 0:
  print("FRULA")
else:
  print(''.join(reversed(curr)))
