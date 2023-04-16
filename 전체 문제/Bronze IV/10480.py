for i in range(int(input())):
    num = int(input())
    s = 'odd'
    if num % 2 == 0:
        s = 'even'
    print(f'{num} is {s}')
