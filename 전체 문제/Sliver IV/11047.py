N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

money, use = 0, 0

for i in reversed(coins):
    m = (K - money) // i
    money += i * m
    use += m

    if money == K: break

print(use)
