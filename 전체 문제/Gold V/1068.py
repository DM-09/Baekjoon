n = int(input())
nodes = list(map(int, input().split()))
remove_node = int(input())
node_list = []


class Node:
  def __init__(self, parent, index):
    self.parent = parent
    self.child = []
    self.index = index

  def add_child(self, new_child):
    self.child.append(new_child)

  def count_leaf(self):
    total = +(len(self.child) == 0)

    for child in self.child:
      total += child.count_leaf()

    return total

  def history_printer(self, history, node, num):
    for child in node.child:
      history.append(("-" * num) + str(child.index))
      self.history_printer(history, child, num + 1)
    return history

  def get_node(self, search_index):
    if self.index == search_index:
      return self
    else:
      for child in self.child:
        r = child.get_node(search_index)
        if r: return r

  def remove_node(self, node):
    parent = self.get_node(node.parent.index)
    parent.child.remove(node)

for i in range(n):
  node_list.append(Node(nodes[i], i))

root = None

for i in range(n):
  c = nodes[i]
  p = node_list[c]
  cur_node = node_list[i]

  if c == -1: root = cur_node; continue
  cur_node.parent = p
  p.add_child(cur_node)

if node_list[remove_node].parent == -1: print(0); exit()

root.remove_node(node_list[remove_node])
print(root.count_leaf())
