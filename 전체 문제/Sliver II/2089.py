from math import *

def c(n, b):
  l = ''
  if n == 0: return '0'
  while n != 0:
    a = ceil(n / b)
    r = n - a * b
    n = a
    l += str(r)
  return l[::-1]

print(c(int(input()), -2))
