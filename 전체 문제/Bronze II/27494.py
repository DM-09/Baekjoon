lottery = ['2', '0', '2', '3']


def check(n):
    strn = str(n)
    index = 0
    for num in strn:
        if num == lottery[index]:
            index += 1
            if index == 4:
                return True
    return False


N = int(input())
count = 0

for i in range(1, N + 1):
    if check(i):
        count += 1

print(count)
