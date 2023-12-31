import math

l = []
N = int(input())
for _ in range(8): l.append([])

l[0] = [2, 3, 5, 7]

def isp(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return 0
    return 1

for a in range(0, 7):
    box = l[a]
    next = l[a+1]

    for i in box:
        s = str(i)
        for j in range(1, 10):
            j = str(j)
            n = int(s + j)
            if isp(n): next.append(n)

print(*l[N-1])
