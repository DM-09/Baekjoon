n, c = map(int, input().split())
a = input().split()

print(*sorted(a, key=lambda x: (-a.count(x), a.index(x))))
