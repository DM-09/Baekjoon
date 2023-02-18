N = int(input())
fruit = {'STRAWBERRY': 0, 'BANANA': 0, 'LIME': 0, 'PLUM': 0}

for i in range(N):
    inp = str(input())
    if inp[0] == 'S':
        fruit[inp[:10]] += int(inp[11:])
    elif inp[0] == 'B':
        fruit[inp[:6]] += int(inp[7:])
    else:
        fruit[inp[:4]] += int(inp[5:])

if fruit['BANANA'] == 5 or fruit['STRAWBERRY'] == 5 or fruit['LIME'] == 5 or fruit['PLUM'] == 5:
    print('YES')
else:
    print('NO')
