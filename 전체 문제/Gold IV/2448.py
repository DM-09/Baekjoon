size = int(input())
s = ['*', '* *', '*****']
step = 3
left_blank = size - 1

while step < size:
  blank = len(s[-1])
  l = []
  for i in s: l.append(i)
  for i in s:
    b = i + ' ' * blank + i
    l.append(b)
    blank -= 2
  s = l
  step *= 2

for i in s:
  b = ' ' * left_blank
  left_blank -= 1
  print(b + i + b)
