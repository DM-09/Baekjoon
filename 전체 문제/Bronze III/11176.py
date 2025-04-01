for t in range(int(input())):
 E, N = map(int, input().split())
 a = 0
 for _ in range(N):
  if int(input()) > E: a += 1
 print(a)
