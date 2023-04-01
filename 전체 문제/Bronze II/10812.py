N, M = map(int, input().split())
basket = [i + 1 for i in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    s = [basket[0:i-1], basket[i-1:k-1], basket[k-1:j], basket[j:]]
    basket = s[0] + s[2] + s[1] + s[3]
print(*basket)
