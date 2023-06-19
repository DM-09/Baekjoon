for i in range(int(input())):
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    print(l[2])
