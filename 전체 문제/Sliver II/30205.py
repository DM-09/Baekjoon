def solve():
    n, m, p = map(int, input().split())
    for _ in range(n):
        a = list(map(int, input().split()))
        mul = a.count(-1)
        a.sort()


        for i in a:
            if i != -1:
                if i <= p: p += i
                else:
                    for _ in range(mul):
                        mul -= 1
                        p *= 2
                        if i <= p: p += i; break
                    else: return 0
        for _ in range(mul):
            mul -= 1
            p *= 2
    return 1

print(solve())
