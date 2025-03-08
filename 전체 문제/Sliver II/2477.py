from collections import deque

k = int(input())
a = deque([list(map(int, input().split())) for _ in range(6)])

t = {'423131' : [0, 1, 3, 4], '423231' : [0, 5, 2, 3], '423141' : [1, 2, 4, 5], '423142' : [2, 3, 0, 5], '424231' : [4, 5, 1, 2] }

while 1:
  if a[0][0] == 4 and a[1][0] == 2: break
  a.rotate(1)

w, x, y, z = t[''.join(str(i[0]) for i in a)]
print((a[w][1] * a[x][1] - a[y][1] * a[z][1]) * k)
