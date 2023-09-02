n, k = map(int, input().split())
num = []

for i in range(n):
    if n % (i + 1) == 0: num.append(i + 1)

if k > len(num): print(0)
else: print(num[k-1])
