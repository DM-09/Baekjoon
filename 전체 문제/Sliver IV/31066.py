for _ in range(int(input())):
    n, m, k = map(int, input().split())
    if n + m + k == 3: print(1); continue
    if m + k == 2: print(-1); continue

    a = m * k
    ans = 1
    n -= a

    while n > 0:
        ans += 2
        n -= a - 1

    print(ans)
