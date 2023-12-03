for _ in range(int(input())):
    n = int(input())
    s = '|' * n

    print(' '.join(s.replace('|||||', '++++  ').split('  ')))
