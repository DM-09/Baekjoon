size = int(input())
s = '*'
step = 1

while step < size:
  k = [c * 3 for c in s] # block
  s = k + [ c + ' ' * step + c for c in s] + k # result
  step *= 3 # 단계
print(' '.join(s))
