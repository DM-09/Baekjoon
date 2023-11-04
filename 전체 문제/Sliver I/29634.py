n, m = map(int, input().split())
l = []

for i in range(n):
  inp = input()
  for j in range(len(inp)):
    if inp[j] == '.':
      l.append([j, i])

ans = -1

while l:
  cur = l.pop()
  todo = [(cur[0], cur[1])]
  count = 1

  while todo:
    c = todo.pop()
    x, y = c[0], c[1]
    for i in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
      if i in l:
        l.remove(i)
        todo.append(i)
        count += 1

  if count > ans: ans = count

print(ans)
