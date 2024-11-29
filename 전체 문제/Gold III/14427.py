import sys
from math import ceil, log2
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
H = int(ceil(log2(n)))+1
tree = [0] + [0] * int(pow(2, H))


def seg(left, right, i):
  if left == right:
    tree[i] = (l[left], left+1)
    return tree[i]
  mid = (left+right) // 2
  tree[i] = min(seg(left, mid, i*2), seg(mid+1, right, i*2+1))
  return tree[i]


def find(start, end, node, idx, val):
  if idx < start or end < idx: 
    return -1
  if start == end: 
    tree[node] = (val, tree[node][1])
    return node
  if start != end:
    mid = (start+end) // 2
    l = find(start, mid, node*2, idx, val)
    r = find(mid+1, end, node*2+1, idx, val)
    if l != -1: 
      return l
    if r != -1: 
      return r


def update(node):
  if node == 0: return 
  twin = node-1 if node % 2 else node+1
  if tree[twin] == 0:
    tree[node//2] = tree[node]
  else: 
    tree[node//2] = min(tree[node], tree[twin])
  update(node//2)

seg(0, n-1, 1)
for _ in range(int(input())):
  q = list(map(int, input().split()))
  if q[0] == 2: print(tree[1][1])
  else:
    _, a, b = q
    idx = find(0, n-1, 1, a-1, b)
    update(idx)
