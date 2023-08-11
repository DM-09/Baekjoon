from math import *

for _ in range(int(input())):
    raw = input().split()
    O, N, T, L = raw[0], int(raw[1]), int(raw[2]), int(raw[3])

    BigO = N

    try:
        if O == 'O(N^2)': BigO = N ** 2
        if O == 'O(N^3)': BigO = N ** 3
        if O == 'O(2^N)': BigO = 2 ** N
        if O == 'O(N!)': BigO = factorial(N)

        print('May Pass.' if BigO * T / 100000000 <= L else 'TLE!')
    except: print('TLE!')
