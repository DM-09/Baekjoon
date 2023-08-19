for _ in range(int(input())):
  n, c = int(input()), []
  for i in [25, 10, 5, 1]:
    need = n // i
    c.append(need)
    n -= need * i
  print(*c)
