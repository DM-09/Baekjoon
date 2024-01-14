n,m=map(int,input().split())
while n:
 if n==m or n+1==m:print('YES');break
 n//=2
else:print('NO')
