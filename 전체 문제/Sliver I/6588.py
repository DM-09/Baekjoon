import sys
input = sys.stdin.readline

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

while 1:
    n = int(input())
    if n == 0: break

    a=i=b=0

    while 1:
        a = box[i+1]
        b = n - a
        i += 1
        if BS(b, box) != -1: break

    print(f'{n} = {a} + {b}')

