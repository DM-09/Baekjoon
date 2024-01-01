n, k = map(int, input().split())
a = list(map(int, input().split()))

pre = 0
ans = 0

for i in a:
    if pre < i: pre = i
    else:
        if pre < i + k: ans += 1
        else: print(-1); break
        pre = i + k
else: print(ans)
