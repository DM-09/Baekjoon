import sys
from math import ceil, log2
input = sys.stdin.readline

n, m, k = map(int, input().split())
l = [int(input()) for _ in range(n)]
H = int(ceil(log2(n)))+1
tree = [0] + [0] * int(pow(2, H))

def seg(left, right, i):
  if left == right:
    tree[i] = l[left]
    return tree[i]
  mid = (left+right) // 2
  tree[i] = seg(left, mid, i*2) + seg(mid+1, right, i*2+1)
  return tree[i]

def seg_sum(start, end, i, left, right):
  if left > end or right < start: return 0
  if left <= start and end <= right: return tree[i]
  mid = (start+end) // 2
  return seg_sum(start, mid, i*2, left, right) + seg_sum(mid+1, end, i*2+1, left, right)

def update(start, end, node, idx, val):
  if idx < start or end < idx: return 0
  tree[node] += val
  if start != end:
    mid = (start+end) // 2
    update(start, mid, node*2, idx, val)
    update(mid+1, end, node*2+1, idx, val)

seg(0, n-1, 1)
for _ in range(m+k):
  q, a, b = list(map(int, input().split()))
  if q == 1:
    update(0, n-1, 1, a-1, b-l[a-1])
    l[a-1] = b
  elif q == 2:  print(seg_sum(0, n-1, 1, a-1, b-1))
