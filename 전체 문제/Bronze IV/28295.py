r = 0

for _ in range(10):
    r += {1: 90, 2: 180, 3: -90}[int(input())]
    r %= 360

print({0: 'N', 90: 'E', 180: 'S', 270: 'W'}[r])
