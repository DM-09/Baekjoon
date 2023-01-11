T = int(input())
x = 0

for i in range(T):
    a, b = input().split()
    a, b = int(a), int(b)
    x = x + 1

    print(f'Case #{x}: {a} + {b} = {a + b}')
