n, l = map(int, input().split())
a = list(map(int, input().split()))

al = 0
last = 0
num = 0

for i in range(n):
    if i >= l:
        al -= a[last]
        last += 1
    al += a[i]
    if al >= 129 and al <= 138: num += 1

print(num)
