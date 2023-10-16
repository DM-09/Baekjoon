n, m = map(int, input().split())
a = list(map(int, input().split()))

def cut(target, a):
    num = 0
    for i in a:
        if target <= i: num += i - target
    return num

start, end = 0, max(a)

while start <= end:
    mid = (start + end) // 2
    result = cut(mid, a)
    if result >= m: start = mid + 1
    else: end = mid - 1

print(end)
