from collections import *
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cloverx = defaultdict(list)
clovery = defaultdict(list)

for _ in range(n):
  x, y = map(int, input().split())
  cloverx[x].append(y)
  clovery[y].append(x)

for i in cloverx: cloverx[i].sort()
for i in clovery: clovery[i].sort()

def BS(target, data, o):
  start, end = 0, len(data) - 1

  while start <= end:
    mid = (start + end) // 2
    if data[mid] == target: return data[mid+o]
    if data[mid] < target: start = mid + 1
    else: end = mid - 1
  return -1

x, y = 0, 0
for m in input().strip():
  if m == 'U': y = BS(y, cloverx[x], 1)
  elif m == 'D': y = BS(y, cloverx[x], -1)
  elif m == 'R': x = BS(x, clovery[y], 1)
  elif m == 'L': x = BS(x, clovery[y], -1)

print(x, y)
