inp = input()
new = ''
for i in range(len(inp)):
    if inp[i].isupper():
        new += inp[i].lower()
    else:
        new += inp[i].upper()
print(new)
