N = int(input())
l = list(map(int, input().split()))
t, ind = [0], 0

l.sort()

for i in l:
    t.append(i + t[ind])
    ind += 1
  
print(sum(t))
