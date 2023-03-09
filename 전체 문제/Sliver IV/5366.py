s = {}
n = []
t = 0

while True:
    inp = input()
    if inp == '0':
        break
    try:
        s[inp] += 1
    except KeyError:
        s[inp] = 1
        n.append(inp)

for i in range(len(n)):
    name = n[i]
    num = s[name]
    t += num
    print(f'{name}: {num}')
print(f'Grand Total: {t}')
