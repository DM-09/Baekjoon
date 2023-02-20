T = int(input())

for _ in range(T):
    F = int(input())
    Ho = int(input())
    house = [i for i in range(1, 15)]

    for _ in range(F):
        for i in range(len(house)-1, 0, -1):
            house[i] = sum(house[0:i+1])

    print(house[Ho-1])
