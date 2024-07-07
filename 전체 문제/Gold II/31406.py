import sys
sys.setrecursionlimit(10**6)

n, query = map(int, input().split())
toggle = [False] * n

class Node:
  def __init__(self, parent, index):
    self.parent = parent
    self.child = []
    self.index = index

  def add_child(self, new_child):
    self.child.append(new_child)

  def get_node(self, search_index):
    if self.index == search_index: return self
    else:
      for child in self.child:
        r = child.get_node(search_index)
        if r: return r

  def cur_list(self, l):
    for i in self.child:
      l.append(i.index)
      if toggle[i.index-1]: i.cur_list(l)
    return l

box = []

for i in range(2, n+2):
  a, *l = map(int, input().split())
  box.append(l)

def append(index, p):
  q = box[index]
  for i in q:
    new = Node(p, i)
    r = append(i-1, new)
    p.add_child(r)
  return p

tree = append(0, Node(None, 1))
curser = 0

for _ in range(query):
  l = tree.cur_list([])
  inp = input().split()
  m = inp[0]
  if m[0] == 't':
    toggle[l[curser]-1] = not toggle[l[curser]-1]
  elif m == 'move':
    curser += int(inp[1])
    if curser < 0: curser = 0
    elif curser > len(l) - 1: curser = len(l) - 1
    print(l[curser])
