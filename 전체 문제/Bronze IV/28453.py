n = int(input())
l = list(map(int, input().split()))
r = ''

for i in l:
    if i >= 300: r += '1'
    elif i >= 275: r += '2'
    elif i >= 250: r += '3'
    else: r += '4'

print(' '.join(r))
