from datetime import *
from collections import *
from bisect import *
import sys

input = sys.stdin.readline

def dateParser(i : str):
  a, b = i.split()
  return int(datetime(*map(int, a.split('-')), *map(int, b.split(':'))).timestamp())

lv_dict = defaultdict(list)
n, q = map(int, input().split())

for _ in range(n):
  d, lv = input().split('#')
  lv_dict[int(lv)].append(dateParser(d))

for i in lv_dict: lv_dict[i].sort()

for _ in range(q):
  start, end, lv = input().split('#')
  s, e, lv = dateParser(start), dateParser(end), int(lv)
  cnt = 0

  for i in lv_dict:
    if i < lv: continue
    cur = lv_dict[i]
    left = bisect_left(cur, s)
    right = bisect(cur, e)

    cnt += right - left

  print(cnt)
