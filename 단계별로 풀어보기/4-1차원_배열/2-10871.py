n, x = input().split()
l = list(map(int, input().split()))
p = ''

for i in range(len(l)):
    if l[i] < int(x):
        p = p + str(l[i]) + ' '


print(p)
