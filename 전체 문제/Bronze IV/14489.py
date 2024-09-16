a, b = map(int, input().split())
c = int(input())
m = a + b

if m >= c*2: m -= c*2
print(m)
