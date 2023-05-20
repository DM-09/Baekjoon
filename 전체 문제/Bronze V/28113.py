N, A, B = map(int, input().split())
n = N + abs(N - B)

if n > A:
    print('Bus')
elif n < A:
    print('Subway')
else:
    print('Anything')
