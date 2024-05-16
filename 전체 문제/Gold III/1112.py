from math import *

def c(n, b):
 l = ""
 k = b > 0 and n < 0
    
 if n == 0: return 0
 if b > 0: n = abs(n)
        
 while n != 0:
  a = n // b if b > 0 else ceil(n / b)
  r = n - a * b
  n = a
  l += str(r)
    
 if k: l += "-"
 return l[::-1]

print(c(*map(int, input().split())))
