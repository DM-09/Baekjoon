t = int(input())
n = int(input())
f = list(map(int, input().split()))

print("Padaeng_i Happy" if sum(f) >= t else "Padaeng_i Cry")
