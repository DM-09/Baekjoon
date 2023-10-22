import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

num = 0

l = [0] * 2000000
for i in a: l[i - 1] = 1

for i in a:
    sub = x - i
    if sub > 0 and l[sub - 1]: num += 1

print(num // 2)
