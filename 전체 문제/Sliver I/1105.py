L, R = map(int, input().split())
num = str(L)
n = list('0' * len(num))

for i in range(len(num)):
    cur = num[i]
    tmp = list(n)

    tmp[i] = '9'

    if L <= int(''.join(tmp)) <= R: cur = '9'
    else:
        number = 7

        while number > -1:
            tmp[i] = str(number)
            if L <= int(''.join(tmp)) <= R:
                cur = str(number)
                break
            number -= 1

    n[i] = cur

print(n.count('8'))
