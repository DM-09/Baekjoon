n, m = map(int, input().split())

l = [input() for _ in range(n)]
num = 0

for _ in range(m):
    i = input()
    if i in l: num += 1

print(num)
