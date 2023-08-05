import sys
input = sys.stdin.readline

def Binary_Search(target, data):
    start, end = 0, len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target: return mid
        if data[mid] < target: start = mid + 1
        else: end = mid - 1
    return -1

a, data = input(), list(map(int, input().split()))
b, targets = input(), list(map(int, input().split()))

data.sort()

for i in targets:
    print(1 if Binary_Search(i, data) != -1 else 0)
