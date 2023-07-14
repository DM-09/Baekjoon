def isVPS(S):
    while S.find('()') != -1:
        S = S.replace('()', '')
    if S == '': return True
    return False

for _ in range(int(input())):
    if isVPS(input()):
        print('YES')
    else:
        print('NO')
