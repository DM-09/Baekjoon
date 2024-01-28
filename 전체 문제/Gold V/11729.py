def hanoi(n, start, mid, target):
  if n > 0:
    hanoi(n - 1, start, target, mid)
    print(start, target)
    hanoi(n - 1, mid, start, target)

n = int(input())
print(2 ** n - 1)
hanoi(n, '1', '2', '3')
