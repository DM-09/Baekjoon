A, B, V = map(int, input().split())
n = V - B
C = A - B

net = n // C

if n % C == 0:
    print(net)
else:
    print(net + 1)
