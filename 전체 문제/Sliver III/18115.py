from collections import deque

n = int(input())
l = list(map(int, input().split()))

a = deque()
b = [n-i for i in range(n)]


for i in range(n):
    cur = l[n-i-1]
    c = b.pop()
    if cur == 1: a.appendleft(c)
    elif cur == 2: a.insert(1, c)
    else: a.append(c)
print(*a)
