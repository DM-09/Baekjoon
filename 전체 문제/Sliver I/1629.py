a, b, c = map(int, input().split())

def fpow(a, b, c):
  if b == 1:
    return a % c
  else:
    if b % 2 == 0:
      return (fpow(a, b//2, c) ** 2) % c
    else:
      return ((fpow(a, b//2, c) ** 2) * a) % c

print(fpow(a, b, c))

