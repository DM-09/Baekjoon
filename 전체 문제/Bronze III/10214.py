for i in range(int(input())):
    y, k = 0, 0
    for _ in range(9):
        s1, s2 = map(int, input().split())
        y += s1
        k += s2
    if y > k:
        print('Yonsei')
    elif y < k:
        print('Korea')
    else:
        print('Draw')
