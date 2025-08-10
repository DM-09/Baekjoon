def part_xor(a, b):
  x = a
  for i in range(a+1, b+1): x ^= i
  return x

def xor(a, b):
  start = 2
  if (b-b%2)//2 % 2: start += a+4 - a%4 if a % 4 else a
  else: start = a+4 - a%4

  if b % 2: return part_xor(a, start-1)^(b-1)^b
  else: return part_xor(a, start-1)^b

for _ in range(int(input())): print(xor(*map(int, input().split())))
