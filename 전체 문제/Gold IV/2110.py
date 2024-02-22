import sys
input = sys.stdin.readline

n, c = map(int, input().split())
l = sorted([int(input()) for _ in range(n)])

start, end = 1, l[-1] - l[0]
r = 0

while start <= end:
  mid = (start + end) // 2
  count = 1
  last = l[0]
  for i in range(1, n):
    if l[i] - last >= mid: count += 1; last = l[i]

  if count < c: end = mid - 1
  else: start = mid + 1; r = max(r, mid)

print(r)
