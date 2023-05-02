a, b = map(int, input().split())
m = str(a // b) + '.'

for _ in range(1001):
    a = (a % b) * 10
    m += str(a // b)
print(m)
