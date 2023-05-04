s = []

for i in range(7):
    n = int(input())
    if n % 2 != 0: s.append(n)

if len(s) == 0:
    print(-1)
else:
    print(sum(s))
    print(min(s))
