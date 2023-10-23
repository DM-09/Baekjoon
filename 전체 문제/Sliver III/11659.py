import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

sumBox = [0] * (n + 1)

for i in range(n):
    sumBox[i + 1] = sumBox[i] + a[i]
    
for _ in range(m):
    i, j = map(int, input().split())
    print(sumBox[j] - sumBox[i - 1])
