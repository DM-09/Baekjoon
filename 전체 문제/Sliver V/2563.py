num = int(input())

paper_space = [[0 for i in range(100)] for i in range(100)]

for i in range(num):
  x_start, y_start = map(int, input().split())
  
  for y in range(10):
    for x in range(10):
      paper_space[y_start + y][x_start + x] = 1

print(sum(map(sum, paper_space)))
