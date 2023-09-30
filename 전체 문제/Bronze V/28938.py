m = int(input())
a = sum(list(map(int, input().split())))

if a == 0: print('Stay')
else: print('Right' if a > 0 else 'Left')
