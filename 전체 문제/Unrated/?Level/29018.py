def sort(e):
    t = 0
    if e.isdigit(): t = 2
    elif e.isupper(): t = 1
    return (t, e)

while True:
    inp = input()
    if inp == '#': break
    print(''.join(sorted(list(inp), key= lambda x: sort(x))))
