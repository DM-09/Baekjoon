def Binary_Search(target, data):
    start, end = 0, len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target: return 1
        if data[mid] < target: start = mid + 1
        else: end = mid - 1
    return 0

for _ in range(int(input())):
    n1, a1 = int(input()), list(map(int, input().split()))
    n2, a2 = int(input()), list(map(int, input().split()))

    a1.sort()

    for i in a2: print(Binary_Search(i, a1))
