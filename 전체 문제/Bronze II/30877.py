import sys
input = sys.stdin.readline

r = ''

for _ in range(int(input())):
    s, t = input().split()

    for i in range(len(s)):
        if s[i] in 'Xx':
            print(t[i].upper(), end='')
            break
