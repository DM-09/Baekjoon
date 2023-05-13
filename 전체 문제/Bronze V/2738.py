import sys

input = sys.stdin.readline
N, M = map(int, input().split())
l = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
  l[i] = list(map(int, input().split()))

  
for i in range(N):
  m_list = list(map(int, input().split()))
  for j in range(M):
    l[i][j] += m_list[j]
  

for i in l:
  print(*i)
