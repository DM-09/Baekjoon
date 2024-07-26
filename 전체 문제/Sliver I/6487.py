from fractions import Fraction as Fra

inf = float('inf')


def make_formula(x1, y1, x2, y2):
  if x1 == x2: return inf, x1
  if y1 == y2: return 0, y1

  a = Fra((y1 - y2), (x1 - x2))
  b = y1 - x1 * a
  return a, b


for _ in range(int(input())):
  x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
  a1, b1 = make_formula(x1, y1, x2, y2)
  a2, b2 = make_formula(x3, y3, x4, y4)

  if a1 == a2 and b1 == b2: print('LINE')
  elif a1 == a2 and b1 != b2: print('NONE')
  else:
    if a1 == inf: sol_x = b1
    elif a2 == inf: sol_x = b2
    else: sol_x = Fra((b2 - b1), (a1 - a2))

    if a1 == 0: sol_y = b1
    elif a2 == 0: sol_y = b2
    else: sol_y = eval(str(a1 * Fra(sol_x) + b1))

    if type(sol_x).__name__[0] == 'F':
      a = str(sol_x).split("/")
      b = a[1] if len(a) > 1 else 1
      sol_x = int(a[0]) / int(b)

    print('POINT {:.2f} {:.2f}'.format(sol_x, sol_y))
