num = int(input())
n = 2
e = 1

if num == 1:
    print(1)
else:
    for i in range(num):
        if n <= num <= (n + e * 6 - 1):
            print(e + 1)
            break
        n += e * 6
        e += 1
