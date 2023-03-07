while True:
    i = list(map(int, input().split()))
    if i[0] == 0 and i[1] == 0:
        break
    if i[0] > i[1]:
        print('Yes')
    else:
        print('No')
