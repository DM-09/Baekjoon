i, j, k = map(int, input().split())
a, b, c = 0, 0, 0
y = 0

while True:
    a += 1; b += 1; c += 1
    y += 1
    
    if a > 15: a = 1
    if b > 28: b = 1
    if c > 19: c = 1
    
    if i == a and j == b and k == c:
        print(y)
        break
