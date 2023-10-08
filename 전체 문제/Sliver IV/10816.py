def Binary_Search(target, data):
    start, end = 0, len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target: return i
        if data[mid] < target: start = mid + 1
        else: end = mid - 1
    return '@'

d = {}
n = int(input())
a = list(map(int, input().split()))

for i in a:
    try: d[i] += 1
    except: d[i] = 1

a.sort()

m = int(input())

for i in list(map(int, input().split())): print(d.get(Binary_Search(i, a), 0), end=' ')
