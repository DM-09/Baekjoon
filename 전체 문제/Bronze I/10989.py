import sys
input = sys.stdin.readline

l = [0] * 10001
for _ in range(int(input())): l[int(input())] += 1
for i in range(1, len(l)):
    for j in range(l[i]): print(i)
