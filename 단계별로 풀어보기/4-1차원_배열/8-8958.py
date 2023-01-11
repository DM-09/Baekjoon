n = input()

for i in range(int(n)):
    inp = input()

    result = 0
    num = 0
    for j in range(len(inp)):
        if inp[j] == 'O':
            num += 1
        else:
            num = 0
        result += num
    print(result)
    result = 0
