num = int(input())

for _ in range(num):
  m = int(input())
  x, y = 0, 0
  while m > (2 ** (y + 1)):
    y += 1
    
  m = m - (2 ** y)

  while m >= (2 ** x):
    x += 1
  x -= 1
  
  print(x, y)
