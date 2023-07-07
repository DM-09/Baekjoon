while True:
    try:
        a, b = input().split()
        a = list(a)
        ind = 0

        for i in b:
            if i == a[ind]:
                ind += 1
            if ind == len(a):
                print('Yes')
                break
        else:
            print('No')
    except:
        break
