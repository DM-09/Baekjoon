n = int(input())
a = list(map(int, input().split()))

odd, even = 0, 0

for i in a:
    if i % 2 == 0: even += 1
    else: odd += 1

print('Happy' if even > odd else 'Sad')
