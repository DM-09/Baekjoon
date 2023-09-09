n = int(input())
ps = list(map(int, input().split()))
b = [[], [], [], [], []]

for _ in range(n):
    k, t = map(int, input().split())
    b[k-1].append(t)
    
a = []
for i in b: a.append(sorted(i))

tt, ind = 0, 0

for i in range(5):
    c = ps[i]
    diff = a[i][0]
    tt += 60
    
    for j in range(len(a[i])):
        if j == c: break
        cc = a[i][j]
        tt += cc - diff + cc
        diff = cc
        
print(tt - 60)
