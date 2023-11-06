k, n = map(int, input().split())
l = [int(input()) for _ in range(k)]

start, end = 1, max(l)

while start <= end:
    mid = (start + end) // 2
    re = 0

    for i in l: re += i // mid

    if re >= n: start = mid + 1
    else: end = mid - 1

print(end)
