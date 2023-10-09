n = int(input())
l = sorted([int(input()) for _ in range(n)])
c = 0

for i in range(n // 3):
    c += l.pop() + l.pop()
    l.pop()
print(c + sum(l))
