a = input()
b = list(input())

while len(b) != len(a):
  if b.pop() == 'B': b = b[::-1]

print(+(''.join(b)==a))
