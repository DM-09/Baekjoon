for _ in range(3):
    n = 0
    for i in range(int(input())):
        n += int(input())
    if n == 0: 
        print(0)
    elif n < 0:
        print('-')
    else:
        print('+')
