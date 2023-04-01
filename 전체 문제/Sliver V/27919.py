N = input()
s = ''

U = N.count('U')
D = N.count('D')
P = N.count('P')
C = N.count('C')

if U + C > -(((D + P) / 2) // -1):
  s += 'U'

if D + P > 0:
  s += 'DP'

if U + D + P + C == 0:
  s = 'C'

print(s)
