n = int(input())
a = list(map(int, input().split()))

cur = a[0]
count = 1

for i in range(1, len(a)):
    c = a[i]
    if cur <= c: count += 1
    cur = c

print(count)
