def SOE(MAX, MIN=1):
    box, l = [], [i + 1 for i in range(MAX)]

    for i in range(MAX):
        c = l[i]
        if c != 1 and c != 0:
            for j in range(2, MAX // c + 1):
                l[c * j - 1] = 0
            if c >= MIN: box.append(c)
    return box

def BS(target, data):
    start, end = 0, len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target: return mid
        if data[mid] < target: start = mid + 1
        else: end = mid - 1
    return -1

box = SOE(1000000)
n = int(input())

a=i=b=0
q=w=0

if n < 8: exit(print(-1))

if n % 2: q=2; w=3; n -= 5
else: q=w=2; n -= 4

if n == 4: exit(print(q, w, 2, 2))
    
while 1:
    a = box[i+1]
    b = n - a
    i += 1
    if BS(b, box) != -1: break

print(a, b, q, w)
