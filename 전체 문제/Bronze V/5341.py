while True:
    i = int(input())
    n = 0
    if i == 0:
        break
    for x in range(i):
        n += i - x
    print(n)
