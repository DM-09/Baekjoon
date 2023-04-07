m = int(input()); d = int(input())

if m < 2:
    print('Before')
elif m == 2:
    if d < 18:
        print('Before')
    elif d == 18:
        print('Special')
    elif d > 18:
        print('After')
elif m > 2:
    print('After')
