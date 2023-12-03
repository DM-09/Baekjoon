import sys
input = sys.stdin.readline

people = [list(map(int, input().split())) for _ in range(int(input()))]
x = 0

for p, c in people:
    if abs(p - x) <= c: x += 1

print(x)
