from queue import PriorityQueue as pq
import sys

input = sys.stdin.readline

t, n = map(int, input().split())
p = pq()

for _ in range(n):
    a, b, c = map(int, input().split())
    box = (-c, a, b)
    p.put(box)

for i in range(t):
    s = p.get()
    box = (s[0] + 1, s[1], s[2] - 1)
    print(s[1])

    if box[2] != 0: p.put(box)
