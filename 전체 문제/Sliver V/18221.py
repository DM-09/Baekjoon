n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

t = []
s = []

for i in range(n):
  for j in range(n):
    if l[i][j] == 5: t = [i, j]
    elif l[i][j] == 2: s = [i, j]

dis = (t[0]-s[0])**2 + (t[1]-s[1])**2
if dis < 25: exit(print(0))

friend = 0
for i in range(min(t[0], s[0]), max(t[0], s[0])+1):
  for j in range(min(t[1], s[1]), max(t[1], s[1])+1):
    if i < n and j < n and l[i][j] == 1: friend += 1

print(+(friend >= 3))
