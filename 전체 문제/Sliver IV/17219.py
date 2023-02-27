N = int(input())
name = []
file = []

for i in range(N):
    inp = input().split('.')
    try:
        index = name.index(inp[1])
        file[index][1] += 1
    except ValueError:
        name.append(inp[1])
        file.append([inp[1], 1])

file.sort()

for f in range(len(file)):
    print(file[f][0] + ' ' + str(file[f][1]))
    
# PyPy3로 제출했습니다
