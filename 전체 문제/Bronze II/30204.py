n, x = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) % x == 0: print(1)
else: print(0)
