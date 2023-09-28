n = int(input())
a = list(map(int, input().split()))

e, o = [], []

for i in a:
    if i % 2 == 0: e.append(i)
    else: o.append(i)

num = sum(e) + sum(o)
o.sort()

for i in range(len(a)):
    if num % 2 == 0: print(num); break
    o.pop(0)
    num = sum(e) + sum(o)
else: print(0)
