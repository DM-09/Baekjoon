num = int(input())

inp = list(map(float, input().split()))

max_num = max(inp)
for i in range(num):
    inp[i] = inp[i] / max_num * 100

print(sum(inp) / num)
