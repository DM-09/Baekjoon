import math

H, M = input().split()
H, M = int(H), int(M)

Added = (H * 60) + (M - 45)

new_H = math.floor(Added / 60)
new_M = Added % 60

print(new_M, Added)


if new_H < 0:
    new_H = 24 + new_H

print(new_H, new_M)
