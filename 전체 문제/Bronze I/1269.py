while True:
    n = int(input())
    if n == 0: break

    re = ''.join(reversed(str(n)))
    print(re)
    print('yes' if str(n) == re else 'no')
