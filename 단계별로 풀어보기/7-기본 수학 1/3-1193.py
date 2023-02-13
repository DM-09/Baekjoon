X = int(input())
num, L, R = 2, 2, 3
a, b = 0, 0

if X == 1:
    print('1/1')
else:
    while True:
        if L <= X <= R:
            a = num - (X - L)
            b = num + 1 - a

            if num % 2 == 0:
                print(f"{b}/{a}")
            else:
                print(f"{a}/{b}")
            break

        num += 1
        L = R + 1
        R += num
