from collections import deque
N = int(input())

if N == 1:
    print('*')
else:
    l = deque(['*****', '*   *', '* * *', '*   *', '*****'])
    a = 5

    for i in range(N - 2):
        for j in range(len(l)):
            l[j] = '* ' + l[j] + ' *'
        a += 4

        l.appendleft('*' + ' ' * (a - 2) + '*')
        l.appendleft('*' * a)
        l.append('*' + ' ' * (a - 2) + '*')
        l.append('*' * a)

    print(*l)
