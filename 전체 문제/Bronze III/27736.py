import math
N = math.ceil(int(input()) / 2)
vote = list(map(int, input().split()))

y, n, x = vote.count(1), vote.count(-1), vote.count(0)

if N <= x:
    print('INVALID')
elif y > n:
    print('APPROVED')
else:
    print('REJECTED')
