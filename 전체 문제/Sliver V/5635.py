h = []
N = int(input())

for i in range(N):
    inp = input().split()
    if int(inp[2]) < 10: inp[2] = '0' + inp[2]
    if int(inp[1]) < 10: inp[1] = '0' + inp[1]
    h1 = f'{inp[3]}{inp[2]}{inp[1]}'
    h.append([int(h1), inp[0]])
    
print(max(h)[1])
print(min(h)[1])
