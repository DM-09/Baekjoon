def myround(x):
  num, dec = str(x).split(".")
  if dec == '5':
    if int(num) % 2 == 0:
      return round(x) + 1

  return round(x)

l = []
n = int(input())

if n == 0:
  print(0)
else:
  for i in range(n):
    l.append(int(input()))
  
  l.sort()
  a = myround(n * 0.15)
  
  if a > 0:
    l = l[a:-a]

  print(myround(sum(l) / len(l)))
