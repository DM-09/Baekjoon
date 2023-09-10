from queue import PriorityQueue as pq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = [pq() for _ in range(11)]

for _ in range(n):
    p, v = map(int, input().split())
    l[p-1].put(v * -1)

for y in range(k):
    for i in range(11):
        g = l[i].get() if l[i].qsize() != 0 else 0
        l[i].put(g + 1 if g < 0 else g)

    if y != k - 1: team = []

print(sum([l[i].get() * -1 for i in range(11)]))
