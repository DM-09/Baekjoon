from queue import *
q = PriorityQueue()

for _ in range(int(input())):
    a = list(map(int, input().split()))
    if a == [0]: print(q.get() * -1 if q.qsize() != 0 else -1)
    else:
        for i in a[1:]: q.put(i * -1)
