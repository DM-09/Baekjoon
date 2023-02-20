N = int(input())
three = 0

while True:
    K = N - 3 * three

    if K % 5 == 0:
        print(K // 5 + three)
        break
    if K == 0:
        print(three)
        break
    elif K < 3:
        print(-1)
        break
    three += 1
