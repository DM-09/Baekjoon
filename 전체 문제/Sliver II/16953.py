a, b = map(int, input().split())
cnt = 0
while True:
  cnt += 1
  if a == b: break
  elif b < a: cnt = -1; break
    
  if b % 2 == 0: b //= 2
  elif b % 10 == 1: b //= 10
  else: cnt = -1; break

print(cnt)
