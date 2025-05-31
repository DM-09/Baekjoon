for _ in range(int(input())):
  n, m = map(int, input().split())
  data = [list(map(int, list(input()))) for _ in range(n)]
  all_surf = sum(sum(i) for i in data)
  dup_surf = 0

  for i in data:
    for j in i:
      if j != 0: dup_surf += j - 1

  for i in range(n-1):
    for j in range(m):
      c1, c2 = data[i][j], data[i+1][j]
      dup_surf += min(c1, c2)

  for i in range(n):
    for j in range(m-1):
      c1, c2 = data[i][j], data[i][j+1]
      dup_surf += min(c1, c2)

  print(all_surf*6 - dup_surf*2)
