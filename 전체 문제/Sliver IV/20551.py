import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]

a.sort()

def BS(target, data):
    start, end = 0, len(data) - 1
    i = n
    r = 0
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target: i = min(i, mid); r = 1
        if data[mid] < target: start = mid + 1
        else: end = mid - 1
    
    if r: return i
    return -1

for _ in range(m):
 q = int(input())
 print(BS(q, a))
