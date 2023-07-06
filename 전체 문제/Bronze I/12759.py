m = [[0, -1, -2], [3, 4, 5], [6, 7, 8]]
f = int(input())
c = f


def is_finish():
    for i in m:
        for j in i:
            if j in [0, -1, -2, 3, 4, 5, 6, 7, 8]: return True
    return False


def is_win():
    for i in m:
        if i[0] == i[1] and i[1] == i[2]:
            return True

    for i in range(3):
        if m[0][i] == m[1][i] and m[1][i] == m[2][i]:
            return True

    if m[0][0] == m[1][1] and m[1][1] == m[2][2]:
        return True
    if m[0][2] == m[1][1] and m[1][1] == m[2][0]:
        return True

    return False


while is_finish():
    x, y = map(int, input().split())
    m[x-1][y-1] = c
    if is_win():
        print(c)
        break
    c = 1 if c == 2 else 2
else:
    print(0)
