point = [list(map(int, input().split())) for _ in range(int(input()))]
print(*sorted(point, key= lambda x: x[1])[0])
