N = int(input())

for i in range(N):
    inp = input().split()
    s1 = inp[0].count(inp[1])
    print(len(inp[0]) - s1 * len(inp[1] )+ s1)
