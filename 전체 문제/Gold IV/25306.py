def xor(a, b):
  x = a
  for i in range(a+1, b+1): x ^= i
  return x

a, b = map(int, input().split())

start = 2
if (b-b%2)//2 % 2: start += a+4 - a%4 if a % 4 else a
else: start = a+4 - a%4

if b % 2: print(xor(a, start-1)^(b-1)^b)
else: print(xor(a, start-1)^b)
