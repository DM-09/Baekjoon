from collections import *
import sys

n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]
quries = [list(map(int, input().split())) for _ in range(int(input()))]

game_board = [['X' for _ in range(m)] for _ in range(n)]

game_board[-2][-1] = 'F'
game_board[-1][-2] = 'F'

for i in range(k):
  game_board[-2-i][-2-i] = 'F'


def can_move(x, y):
  move = []
  result = []
  for i in range(k): move.append([a+k-i, b+k-i])
  move.extend([[a+1, b], [a, b+1]])
  for x, y in move:
    if ((0 <= x < n) and (0 <= y < m)) and board[x][y] == '.':
      result.append([x, y]) 

  return result


for a in range(n-1, -1, -1):
  for b in range(m-1, -1, -1):
    if game_board[a][b] == 'X':
      for x, y in can_move(a, b):
        if game_board[x][y] == 'S': game_board[a][b] = 'F'; break
      else: game_board[a][b] = 'S'

for x, y in quries: print('First' if game_board[x-1][y-1] == 'F' else 'Second')
