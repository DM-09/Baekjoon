import sys
input = sys.stdin.readline

def Binary_Search(target, data):
    start, end = 0, len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target: return 0
        if data[mid] < target: start = mid + 1
        else: end = mid - 1
    return 1

n, m = map(int, input().split())

a = [input().rstrip() for _ in range(n)]
k = [input().rstrip() for _ in range(m)]

k.sort()

def key(s :str):
    name, exten = s.split('.')
    return (name, Binary_Search(exten, k), exten)

print(*sorted(a, key=lambda x: key(x)))
