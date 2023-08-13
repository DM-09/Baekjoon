n = int(input())
l = [int(input()) for _ in range(n)]

l.sort(reverse=True)
l = l[:42]

r = 0

for i in l:
    if i >= 250: r += 5
    elif i >= 200: r += 4
    elif i >= 140: r += 3
    elif i >= 100: r += 2
    elif i >= 60: r += 1

print(sum(l), r)
