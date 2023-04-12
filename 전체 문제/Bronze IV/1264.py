while True:
    i = input().lower()
    if i == '#':
        break
    n = 0
    n += i.count('a')
    n += i.count('e')
    n += i.count('i')
    n += i.count('o')
    n += i.count('u')
    print(n)
