N = int(input())

for i in range(N):
    inp = input().split()
    print(f'Case {i + 1}: ' + str(int(inp[0]) + int(inp[1])))
