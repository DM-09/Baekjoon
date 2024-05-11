import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

class Node:
  def __init__(self, value, parent=None):
    self.value = value
    self.parent = parent
    self.right = None
    self.left = None

  def add(self, node, a_node):
    if a_node.value < node.value:
      if a_node.right != None: return self.add(node, a_node.right)
      a_node.right = node
    else:
      if a_node.left: return self.add(node, a_node.left)
      a_node.left = node

  def print(self, node):
    if node.left: self.print(node.left)
    if node.right: self.print(node.right)
    print(node.value, end=' ')

head = Node(int(input()))

while 1:
  try: a = int(input())
  except: break

  head.add(Node(a), head)

head.print(head)
