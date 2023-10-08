def Similarity(board, h, w):
    wf = ['WBWBWBWB', 'BWBWBWBW'] * 4
    bf = ['BWBWBWBW', 'WBWBWBWB'] * 4

    ws, bs = 64, 64

    for i in range(8):
        for j in range(8):
            cur = board[i + h][j + w]
            if wf[i][j] != cur: ws -= 1
            if bf[i][j] != cur: bs -= 1

    return 64 - max(ws, bs)

n, m = map(int, input().split())
board = [input() for _ in range(n)]
l = []

for i in range(n - 7):
    for j in range(m - 7):
        l.append(Similarity(board, i, j))

print(min(l))
