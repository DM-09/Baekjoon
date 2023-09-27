n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

num = 0

for i in range(n):
    if a[i] <= b[i]: num += 1

print(num)
