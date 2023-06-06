A, B = map(int, input().split())
N = {abs(B - int(input())) for i in range(int(input()))}

N.add(abs(A - B))
m = min(N)

if m == abs(A - B):
    print(m)
else:
    print(1 + m)
