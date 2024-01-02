inp = input().split()
a = int(inp[0].replace('.', ''))
b = int(inp[1])

tail = len(inp[0][inp[0].index('.')+1:])
mul = str(a ** b)
n = len(mul) - tail * b

l = mul[:n]
r = mul[n:]

if inp[0][0] == '0':
    l = '0'; r = mul
    r = '0' * (tail * b - len(r)) + r
print(l + '.' + r)
