print('Gnomes:')
for _ in range(int(input())):
    l = list(map(int, input().split()))
    if l == sorted(l) or l[::-1] == sorted(l):
        print('Ordered')
    else:
        print('Unordered')
