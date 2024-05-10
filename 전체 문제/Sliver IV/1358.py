w, h, x, y, p = map(int, input().split())
r = h / 2

ans = 0

# Pythagoras
def pita(x1, y1, x2, y2):
  return ((x1-x2)**2 + (y1-y2)**2) ** .5

for _ in range(p):
  a, b = map(int, input().split())
  if (x <= a <= x+w and y <= b <= y+h): ans += 1
  elif pita(x, y+r, a, b) <= r or pita(x+w, y+r, a, b) <= r: ans += 1

print(ans)
