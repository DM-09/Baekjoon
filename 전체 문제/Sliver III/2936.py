x, y = map(int, input().split())
mode = 2
full = 15625

if x == 0: mode = 0
elif y == 0: mode = 1

rx, ry = 0, 0

if x < 125 and y < 125:
  a = 250 - max(x, y)
  b = full / a * 2
  if mode == 0: rx = b; ry = 250 - b
  elif mode == 1: ry = b; rx = 250 - b
else:
  b = full / max(x, y) * 2
  if mode == 0: rx = b; ry = 0
  elif mode == 1: ry = b; rx = 0
  else:
    if x > y: rx = 0; ry = 250 - b
    else: ry = 0; rx = 250 - b

print(f"{rx:.2f} {ry:.2f}")
