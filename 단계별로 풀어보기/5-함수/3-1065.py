def check_one_num(num):
    if num < 100:
        return True
    str_num = str(num)
    diff = int(str_num[0]) - int(str_num[1])

    for i in range(2, len(str_num)):
        next_diff = int(str_num[i - 1]) - int(str_num[i])
        if diff != next_diff:
            return False

    return True


n = input()
re = 0

for i in range(1, int(n) + 1):
    if check_one_num(i):
        re += 1

print(re)

