n = int(input())
a = list(map(int, input().split()))
m = int(input())

start, end = 0, max(a)

while start <= end:
    mid = (start + end) // 2
    re = 0

    for i in a:
        if mid > i: re += i
        else: re += mid

    if re > m: end = mid - 1
    else: start = mid + 1

print(end)
