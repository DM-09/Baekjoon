N = int(input())
bn = int(input())

min_press = abs(N - 100)
if bn == 10:
    print(min_press)
elif bn > 0:
    broken_nums = list(input().split())

    for i in range(1000001):
        for char in str(i):
            if char in broken_nums:
                break
        else:
            new_min = len(str(i)) + abs(N - i)
            if min_press > new_min:
                min_press = new_min

    print(min_press)

else:
    print(min(len(str(N)), min_press))
