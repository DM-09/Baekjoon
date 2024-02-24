n, s, w, g = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(g)]
l = n * 4 - 4
ground = [''] * l
bought = [0] * l
city = 0

ground[0] = 'S'
ground[n-1] = 'I'
ground[n*2-2] = 'B'
ground[n*3-3] = 'U'

a = 0
cur = 0
cur_card = 0
poor = 0
stop = 0
win = True

for i in range(l-4):
  inp = input().split()
  inp.append(0)
  inp.append(i+a)
  if ground[i+a] != '': a += 1
  if inp[0] == 'L': city += 1
  inp[1] = int(inp[1])
  ground[i+a] = inp

def move(n):
  global cur, cur_card, poor, stop, ground, cards, s, win
  cur += n

  if cur >= l: s += w * (cur // l)
  cur %= l

  c = ground[cur]
  if c[0] == 'L':
    if not bought[cur] and s >= c[1]:
      s -= c[1]
      c[2] = 1
      bought[cur] = 1
  elif c[0] == 'B': s += poor; poor = 0
  elif c[0] == 'U': cur = 0; s += w
  elif c[0] == 'I': stop = 3
  elif c[0] == 'G':
    card = cards[cur_card]
    if card[0] == 1: s += card[1]
    elif card[0] == 2:
      if s >= card[1]: s -= card[1]
      else: win = False
    elif card[0] == 3:
      if s >= card[1]: s -= card[1]; poor += card[1]
      else: win = False
    elif card[0] == 4: move(card[1])
    cur_card += 1
    cur_card %= g

for _ in range(int(input())):
  d1, d2 = map(int, input().split())
  if stop > 0:
    stop -= 1
    if d1 == d2: stop = 0
    continue
  move(d1 + d2)
  if win == False: print('LOSE'); exit()

a = sum(bought)
if a == city: print('WIN')
else: print('LOSE')
