from collections import defaultdict as dd

class Node:
  def __init__(self, v, left:None, right:None):
    self.right = right
    self.left = left
    self.value = v

d = dd(None)
d['.'] = None

for _ in range(int(input())):
  c, l, r = input().split()
  d[c] = Node(c, l, r)

for k, v in d.items():
  if not v: continue
  l, r = v.left, v.right
  d[k].left = d[l]
  d[k].right = d[r]


def Order(node, s, type):
  if not node: return s
  if type == 1: s += node.value
  if node.left: s = Order(node.left, s, type)
  if type == 2: s += node.value
  if node.right: s = Order(node.right, s, type)
  if type == 3: s += node.value
  return s

r = d['A']
print(Order(r, '', 1))
print(Order(r, '', 2))
print(Order(r, '', 3))
