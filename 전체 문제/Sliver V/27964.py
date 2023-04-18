t = set()
input()
inp = input().split()

for i in range(len(inp)):
    c = inp[i]
    if c[-6::] == 'Cheese':
        t.add(c)

if len(t) >= 4:
    print('yummy')
else:
    print('sad')
