from math import *

n, k = map(int, input().split())
g = gcd(n, k)

if g != 1:
  n, k = n // g, k // g
  
if k == 1 or k == n-1:
  print(0)
else:
  if k > n/2: k = n-k
  print(n * (k-1))
