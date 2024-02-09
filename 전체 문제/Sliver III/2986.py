import math
n = int(input())
a = 0

for i in range(2, int(math.sqrt(n))+1):
  if n % i == 0: a = max(a, n // i, i)

if a == 0: print(n-1)
else: print(n - a)
